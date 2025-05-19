This project is based on https://github.com/zoom/rtms-developer-preview-js

# Zoom RTMS Saving Raw Video Stream project

This project demonstrates real-time video stream, capture and saving onto local storage using the Zoom RTMS . It focuses on capturing video data from Zoom meetings and saving it to the format received as-is. This sample uses the payload to subscribe to H264 video format.

## Prerequisites

Before running the application, ensure you have the following environment variables set in a `.env` file:
- `ZM_RTMS_CLIENT`: Your Zoom OAuth Client ID (required)
- `ZM_RTMS_SECRET`:Your Zoom OAuth Client Secret (required)

### Additional Environment Variables:
- `PORT`: The port on which the server runs (default: 8080)

## Implementation Details

The application follows this sequence:

1. Starts an server on port 8080
2. Listens for webhook events at `/` endpoint
3. Handles URL validation challenges from Zoom
4. When a meeting starts:
   - Receives `meeting.rtms_started` event
   - Establishes WebSocket connection to signaling server
   - Sends handshake with authentication signature
   - Receives media server URL from signaling server
   - Establishes WebSocket connection to media server
   - Sends media handshake with authentication
   - Begins receiving all media data type (Audio, Video, Deskshare, Transcript, Chat etc...)
5. During the meeting:  
   - Maintains WebSocket connections with keep-alive messages
   - Receives and stores raw video data chunks
   - Stores the chunk into the recordings/{meetingUuid}/{user_id}.raw
   - Handles any connection errors
6. When a meeting ends:  
   - Receives `meeting.rtms_stopped` event
   - Closes all active WebSocket connections

## Running the Application

1. Start the server:
   ```bash
   node index.js  
   ```

2. Start a Zoom meeting. The application will: 
   - Receive the `meeting.rtms_started` event
   - Establish WebSocket connections
   - Begin capturing video data
   - Append the video chunks into .raw file every video stream data is received

## Project-Specific Features  

- Real-time video data capture (H264, HD, 25fps)
- WebSocket connection management for both signaling and media servers
- Meeting Uuid based folder creation and recording to unique filenames
- Keep-alive message handling
- Error handling for WebSocket connections
- URL validation handling

## Project-Specific Notes  

- The application subscribes to video data at 25fps, 720p HD and H264 format
- Video data is not converted, and is directly appended to a local .raw file
- raw files are saved with the naming format: `{user_id}.raw`
- Server runs on port 8080 by default, if PORT is not specificed in .env
- Webhook endpoint is available at `http://localhost:PORT/`

## Additional Setup Requirements  

1. **Node.js** (v14 or higher recommended)
32. **ngrok** for exposing your local server to the Internet
4. **Zoom App** configuration with RTMS scopes enabled

## Troubleshooting  

1. **No Video Files Generated**:
   - Check that you are converting the raw video data to base64 buffer before saving it to local storage
   - Check that the Zoom app has the correct RTMS scopes
   - Check that you have the correct folders created. `recordings` folder should be present in the root directory
   - Ensure the webhook URL is correctly configured in the Zoom app

2. **Connection Issues**:
   - Verify ngrok is running and the tunnel is active
   - Check that the Zoom app credentials in `.env` are correct
   - Ensure the webhook endpoint is accessible from the internet

3. **Video Quality Issues**:
   - The application captures video at 25fps, 720p HD
   - Bandwidth restriction and quality might affect the resolution and framerate of the received stream


## Dependencies

- `@zoom/rtms`: Zoom's Real-Time Media SDK
- `dotenv`: Environment variable management


**SDK Installation Issues**:
   - Make sure you have the correct token for fetching prebuilt binaries
   - Check that you've installed the SDK correctly: `npm install github:zoom/rtms`
