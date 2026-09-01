import os
import json
from datetime import datetime

import requests
import streamlit as st


# API Gateway configuration
API_GATEWAY_BASE_URL = os.getenv("API_GATEWAY_BASE_URL")
STREAM_NAME = os.getenv("KINESIS_STREAM_NAME", "applog1")


if not API_GATEWAY_BASE_URL:
    st.error("API_GATEWAY_BASE_URL environment variable is not configured.")
    st.stop()


API_URL = f"{API_GATEWAY_BASE_URL}/{STREAM_NAME}"


# Generate event timestamp
current_time = datetime.now()
event_timestamp_ms = int(current_time.timestamp() * 1000)
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")


# Simulated application event data
event_data = [
    {
        "event_name": "zb_app_install",
        "gtmLongTime": event_timestamp_ms,
        "base_dt": formatted_time,
        "item_id": "10310425",
        "screen_name": "Permission Request",
    },
    {
        "event_name": "view_item",
        "gtmLongTime": event_timestamp_ms,
        "base_dt": formatted_time,
        "item_id": "10442413",
        "screen_name": "My Information",
    },
    {
        "event_name": "zb_dialog_show",
        "gtmLongTime": event_timestamp_ms,
        "base_dt": formatted_time,
        "item_id": "10493118",
        "screen_name": "Change Phone Number",
    },
    {
        "event_name": "zb_screen_list_click",
        "gtmLongTime": event_timestamp_ms,
        "base_dt": formatted_time,
        "item_id": "10465756",
        "screen_name": "Change Password",
    },
    {
        "event_name": "oneroom_filter_results",
        "gtmLongTime": event_timestamp_ms,
        "base_dt": formatted_time,
        "item_id": "10420590",
        "screen_name": "Change Name",
    },
    {
        "event_name": "zb_app_install",
        "gtmLongTime": event_timestamp_ms,
        "base_dt": formatted_time,
        "item_id": "10238586",
        "screen_name": "Login",
    },
    {
        "event_name": "screen_view",
        "gtmLongTime": event_timestamp_ms,
        "base_dt": formatted_time,
        "item_id": "10432617",
        "screen_name": "Find Password",
    },
    {
        "event_name": "zb_vr_loading",
        "gtmLongTime": event_timestamp_ms,
        "base_dt": formatted_time,
        "item_id": "10435194",
        "screen_name": "Login Email",
    },
    {
        "event_name": "zb_view_contents",
        "gtmLongTime": event_timestamp_ms,
        "base_dt": formatted_time,
        "item_id": "10456187",
        "screen_name": "Find Email",
    },
    {
        "event_name": "user_engagement",
        "gtmLongTime": event_timestamp_ms,
        "base_dt": formatted_time,
        "item_id": "10440393",
        "screen_name": "Email Verification",
    },
    {
        "event_name": "zb_screen_click",
        "gtmLongTime": event_timestamp_ms,
        "base_dt": formatted_time,
        "item_id": "10478202",
        "screen_name": "Authentication",
    },
    {
        "event_name": "sign_up",
        "gtmLongTime": event_timestamp_ms,
        "base_dt": formatted_time,
        "item_id": "10446125",
        "screen_name": "Main",
    },
    {
        "event_name": "apt_filter_results",
        "gtmLongTime": event_timestamp_ms,
        "base_dt": formatted_time,
        "item_id": "10469918",
        "screen_name": "Contact Us",
    },
    {
        "event_name": "session_start",
        "gtmLongTime": event_timestamp_ms,
        "base_dt": formatted_time,
        "item_id": "10171775",
        "screen_name": "Send Message",
    },
    {
        "event_name": "view_item",
        "gtmLongTime": event_timestamp_ms,
        "base_dt": formatted_time,
        "item_id": "10450963",
        "screen_name": "Splash",
    },
    {
        "event_name": "ecommerce_purchase",
        "gtmLongTime": event_timestamp_ms,
        "base_dt": formatted_time,
        "item_id": "10393346",
        "screen_name": "Apartment Search",
    },
]


def send_event(event):
    """Send an application event to the API Gateway endpoint."""

    payload = json.dumps(event)

    response = requests.post(
        API_URL,
        data=payload,
        headers={"Content-Type": "application/json"},
        timeout=10,
    )

    return response


# Streamlit application
st.title("Application Event Log Generator")

st.write(
    "Select an application event to send a simulated event "
    "through the AWS real-time ingestion pipeline."
)

st.caption(f"Target Kinesis stream: `{STREAM_NAME}`")


# Display events as a button grid
columns = st.columns(4)

for index, event in enumerate(event_data):
    with columns[index % 4]:
        if st.button(event["screen_name"], key=f"event_{index}"):
            try:
                response = send_event(event)

                if response.ok:
                    st.success(
                        f"Event sent successfully: `{event['event_name']}`"
                    )
                else:
                    st.error(
                        f"Request failed with status code {response.status_code}"
                    )

            except requests.RequestException as error:
                st.error(f"Failed to send event: {error}")
