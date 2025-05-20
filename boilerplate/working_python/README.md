# Print Incoming Audio Example

This example demonstrates how to receive and print incoming audio data from a Zoom meeting using the RTMS (Real-Time Media Streaming) service.

## Prerequisites

- Python 3.7 or higher
- A Zoom account with RTMS enabled
- Zoom App credentials (Client ID and Client Secret)
- Zoom Secret Token for webhook validation

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

1. Start the server:
```bash
python start.py
```

2. The server will start on port 3000. You'll need to expose this port to the internet using a tool like ngrok:
```bash
ngrok http 3000
```

3. Configure your Zoom App's webhook URL to point to your exposed endpoint (e.g., `https://your-ngrok-url/webhook`)

4. Start a Zoom meeting and enable RTMS. The server will receive and print the incoming audio data.

## How it Works

1. The server listens for webhook events from Zoom
2. When RTMS starts, it establishes WebSocket connections to Zoom's signaling and media servers
3. Audio data is received through the media WebSocket connection
4. The raw audio data is printed to the console in hexadecimal format

## Notes

- This is a basic example that prints the raw audio data. In a production environment, you would typically process or save this data.
- The server handles both signaling and media WebSocket connections
- Keep-alive messages are automatically responded to maintain the connection 