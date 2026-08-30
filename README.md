# Real-Time Data Ingestion Pipeline on AWS

A real-time data ingestion pipeline built with Amazon API Gateway, Kinesis Data Streams, Kinesis Data Firehose, and Amazon S3.

## Overview

This project implements a real-time data ingestion pipeline using AWS managed services.

The pipeline receives streaming data through an API endpoint, processes the data using Amazon Kinesis, and delivers the data to Amazon S3 for persistent storage.

## Project Objectives

- Build a real-time data ingestion pipeline on AWS
- Understand the architecture of streaming data ingestion
- Configure Amazon API Gateway for data collection
- Stream data using Amazon Kinesis Data Streams
- Deliver streaming data to Amazon S3 using Amazon Kinesis Data Firehose
- Understand how different AWS services work together in a data pipeline

## Architecture

> Architecture diagram will be added after the pipeline is completed.

## Technology Stack

- Amazon API Gateway
- Amazon Kinesis Data Streams
- Amazon Kinesis Data Firehose
- Amazon S3
- Python
- Streamlit

## Data Flow

```text
Streamlit
    ↓
API Gateway
    ↓
Kinesis Data Streams
    ↓
Kinesis Data Firehose
    ↓
Amazon S3
