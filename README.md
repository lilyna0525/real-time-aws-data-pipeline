# Real-Time Application Log Ingestion Pipeline on AWS

A real-time application event logging pipeline using Streamlit, Amazon API Gateway, Amazon Kinesis Data Streams, Kinesis Data Firehose, and Amazon S3.

## Overview

This project demonstrates how application event logs can be collected and streamed in real time using AWS managed services.

A Streamlit application generates simulated user event data and sends the events to an API Gateway endpoint through HTTP POST requests. Amazon API Gateway transforms the incoming requests and forwards them to an Amazon Kinesis Data Stream for real-time ingestion.

The project focuses on understanding the architecture and implementation of a scalable event data collection pipeline.

## Project Objectives

- Build a real-time application event logging pipeline
- Generate simulated application event data
- Send event data through an HTTP API
- Configure API Gateway to integrate with Kinesis Data Streams
- Transform incoming JSON requests using API Gateway mapping templates
- Use a dynamic stream name as a request parameter
- Stream application events into Kinesis in real time

## Architecture

![Real-Time Application Log Ingestion Pipeline](architecture.png)

## Technology Stack

- Amazon API Gateway
- Amazon Kinesis Data Streams
- Amazon Kinesis Data Firehose
- Amazon S3
- Python
- Streamlit

## Data Flow

1. Streamlit generates simulated application events.
2. The application sends event data to an API Gateway endpoint using an HTTP POST request.
3. API Gateway transforms the incoming JSON request.
4. The transformed payload is encoded and sent to Kinesis Data Streams.
5. Kinesis receives and streams the event data for downstream processing and storage.

## Implementation

### 1. Test Data Generation

<img width="967" height="870" alt="image" src="https://github.com/user-attachments/assets/32eb797d-765a-43d9-8c82-b86be51f1397" />

A Streamlit application was developed to generate simulated application event logs.

Each event contains attributes such as:

- Event name
- Timestamp
- Item ID
- Screen name

The application presents the events as a button grid, allowing individual events to be triggered manually for testing.

### 2. Streamlit Event Producer

The Streamlit application uses Python to generate event data and send HTTP POST requests.
The `requests` library is used to communicate with the API Gateway endpoint.

### 3. API Gateway Configuration

<img width="1792" height="437" alt="Screenshot 2026-08-31 at 3 25 20 PM" src="https://github.com/user-attachments/assets/79987410-3884-46f1-9089-b3fe85523638" />

Amazon API Gateway was configured to receive HTTP requests from the Streamlit application.

The API integration uses the `Content-Type` header and a mapping template to transform the incoming JSON payload into the format required by Kinesis.

### 4. Request Transformation

The API Gateway mapping template was configured to transform the incoming JSON request into the format required by Amazon Kinesis Data Streams.

The mapping template performs the following operations:

- Extracts the incoming JSON payload
- Encodes the event data using Base64
- Assigns a partition key
- Dynamically specifies the target Kinesis data stream

#### Dynamic Stream Selection

The Kinesis stream name was passed as a request parameter instead of being hard-coded in the API Gateway integration.

This allows the target stream to be specified dynamically through the API request.

```text
API Request
    ↓
stream-name parameter
    ↓
API Gateway
    ↓
Target Kinesis Data Stream
```

This approach provides greater flexibility when testing the API integration with different Kinesis streams.

#### Partition Key

The `X-Amzn-Trace-Id` request parameter was used as the partition key for Kinesis records during this exercise.

The partition key determines how records are distributed across the shards of a Kinesis Data Stream.

For this project, the partition key was configured as follows:

```text
PartitionKey = X-Amzn-Trace-Id
```

This configuration was used for the purpose of the exercise and may be replaced with an application-specific partitioning strategy in a production environment.

### 5. Kinesis Data Streams

<img width="1792" height="382" alt="Screenshot 2026-08-31 at 3 25 51 PM" src="https://github.com/user-attachments/assets/6ac94ecd-0941-48b3-835d-5a20a49b44dd" />

Amazon Kinesis Data Streams was used as the real-time streaming layer.

The service receives application event records from API Gateway and makes them available for downstream processing.

## Testing

The API endpoint was tested using `curl` with a JSON payload.

Example:

curl -d '{"value":"30","type":"Tip 3"}' \
-H "Content-Type: application/json" \
-X POST <API_GATEWAY_ENDPOINT>

The Streamlit application was also used to trigger different event types and verify that the requests were successfully sent through the pipeline.

## Key Learnings
- Understanding the role of API Gateway in a data ingestion architecture
- Integrating API Gateway with Amazon Kinesis Data Streams
- Using API Gateway mapping templates to transform request data
- Understanding Base64 encoding for Kinesis records
- Passing dynamic parameters through an API request
- Generating and sending event data using Python and Streamlit
- Understanding the architecture of real-time event data ingestion

## Challenges & Troubleshooting

No significant troubleshooting issues were encountered during the implementation.

## Improvements

Potential improvements include:

- Add request validation and error handling
- Add authentication and authorisation to the API endpoint
- Implement structured logging and monitoring
- Add automated data validation
- Introduce downstream processing using AWS Lambda or Amazon Data Firehose
- Improve the event schema for production use

## Results

<img width="1792" height="516" alt="Screenshot 2026-08-31 at 3 24 50 PM" src="https://github.com/user-attachments/assets/ab1ecb45-fa70-49ce-8776-deca604cb22d" />

## Conclusion

This project provided hands-on experience in building a real-time application event ingestion pipeline using AWS managed services.

The project demonstrated how application-generated events can be collected through an API endpoint and streamed into Amazon Kinesis for downstream processing.
