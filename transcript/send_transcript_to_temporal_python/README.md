# Send Incoming Transcripts to Temporal Example

This example demonstrates how to receive and print incoming transcript data from a Zoom meeting using the RTMS (Real-Time Media Streaming) service.

## Prerequisites

- Python 3.7 or higher
- A Zoom account with RTMS enabled
- Zoom App credentials (Client ID and Client Secret)
- Zoom Secret Token for webhook validation
- The [Temporal dev server](https://learn.temporal.io/getting_started/python/dev_environment/#set-up-a-local-temporal-service-for-development-with-temporal-cli)

## Setup

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file in the same directory with your Zoom credentials:
```
ZOOM_SECRET_TOKEN=your_secret_token
ZM_CLIENT_ID=your_client_id
ZM_CLIENT_SECRET=your_client_secret
```

## Running the Example

1. Start a Temporal dev server:
```bash
temporal server start-dev
```

2. Start the app:
```bash
python print_transcripts.py
```

3. The server will start on port 3000. You'll need to expose this port to the internet using a tool like ngrok:
```bash
ngrok http 3000
```

4. Configure your Zoom App's webhook URL to point to your exposed endpoint (e.g., `https://your-ngrok-url/webhook`)

5. Start the Temporal Worker to handle this Workflow:
```bash
python temporal_worker.py
```

6. Start a Zoom meeting and enable RTMS. The server will receive and print the incoming transcript data.

## How it Works

1. The server listens for webhook events from Zoom
2. When RTMS starts, it establishes WebSocket connections to Zoom's signaling and media servers
3. Transcript data is received through the media WebSocket connection
4. The raw transcript data is sent to a [Temporal Workflow](https://docs.temporal.io/workflows) using [signals](https://docs.temporal.io/develop/python/message-passing#signals)
5. You can monitor the running Temporal Workflow in your local Web UI at [http://localhost:8233](http://localhost:8233).
6. Build on this example to do something else with the Workflow :)

## Notes

- The server handles both signaling and media WebSocket connections
- Keep-alive messages are automatically responded to maintain the connection
- The transcript data is received in real-time as participants speak in the meeting 