# Zoom RTMS Samples Repository

This repository contains sample projects demonstrating how to work with Zoom's Realtime Media Streams (RTMS) in JavaScript, Python, and SDK implementations. 

> **Note on Terminology:** Throughout this repository, we standardize on using "Realtime" as a single word (not "Real-Time" or "real-time") for consistency. Some sample files may still use the hyphenated version, which will be updated in future releases.

## Repository Structure

```
.
├── audio/
│   ├── print_audio/
│   ├── print_audio_js/                                        # Print audio using JavaScript
│   ├── print_audio_python/                                    # Print audio using Python
│   ├── print_audio_sdk/                                       # Print audio using SDK
│   ├── save_audio/
│   ├── save_audio_js/                                        # Save audio using JavaScript
│   ├── save_audio_python/                                    # Save audio using Python
│   ├── save_audio_sdk/                                       # Save audio using SDK
│   ├── send_audio_to_assemblyai_transcribe_service_js/      # Transcribe using AssemblyAI
│   ├── send_audio_to_aws_transcribe_service_js/             # Transcribe using AWS (JS)
│   ├── send_audio_to_aws_transcribe_service_sdk/            # Transcribe using AWS (SDK)
│   ├── send_audio_to_azure_speech_to_text_service_js/       # Transcribe using Azure (JS)
│   ├── send_audio_to_azure_speech_to_text_service_sdk/      # Transcribe using Azure (SDK)
│   └── send_audio_to_deepgram_transcribe_service_js/        # Transcribe using Deepgram
├── cloud_streaming/
│   └── stream_to_aws_kinesis_video_stream_js/               # Stream to AWS Kinesis
├── cloud_storage/
│   ├── save_audio_and_video_to_aws_s3_storage_js/          # Save to AWS S3
│   └── save_audio_and_video_to_azure_blob_storage_js/       # Save to Azure Blob Storage
├── live_streaming/
│   ├── stream_audio_and_video_to_custom_frontend_js/        # Stream to custom frontend
│   └── stream_audio_and_video_to_youtube_js/                # Stream to YouTube
├── local_recording/
│   ├── record_audio_and_video_to_local_storage_js/          # Basic local recording
│   └── record_audio_and_video_to_local_storage_advance_js/  # Advanced local recording
├── transcript/
│   ├── print_incoming_transcripts_js/                       # Print transcripts using JavaScript
│   ├── print_incoming_transcripts_python/                   # Print transcripts using Python
│   ├── print_transcripts_sdk/                               # Print transcripts using SDK
│   └── save_transcript_js/                                  # Save transcripts using JavaScript
└── video/
    ├── detect_object_using_tensorflow_js/                   # Object detection using TensorFlow (JS)
    ├── detect_object_using_tensorflow_sdk/                  # Object detection using TensorFlow (SDK)
    ├── save_video_js/                                       # Save video using JavaScript
    └── save_video_sdk/                                      # Save video using SDK
```

## What is RTMS?

Zoom Realtime Media Streams (RTMS) allows developers to access realtime media data from Zoom meetings, including:
- Audio streams
- Video streams
- Meeting transcripts

## Implementation Approaches

### 1. SDK-Based Implementation
The RTMS SDK provides a simplified way to integrate with RTMS by handling many low-level details automatically. Benefits include:
- Simplified integration with just a few function calls
- Automatic connection management
- Built-in error handling and reconnection logic
- Cross-platform compatibility

### 2. Native Implementation
The native implementation gives you more control and customization options by working directly with RTMS. This approach requires:
- Manual webhook event handling
- Direct websocket connection management
- Custom error handling
- Raw data processing

## Creating an App in the Zoom Marketplace

To use these samples, you'll need to create an app in the Zoom Marketplace. Here's how:

1. **Sign in to the Zoom Marketplace**:
   - Go to https://marketplace.zoom.us/
   - Sign in with your RTMS beta-enabled account

2. **Create a New App**:
   - Select Develop → Build App → General App
   - Click Create
   - Select "User-Managed"

3. **Configure Basic Information**:
   - [Optional] In the basic information section, provide your OAuth Redirect URL
   - You can use the redirect URL generated from ngrok

4. **Configure Event Subscriptions**:
   - Navigate to Features → Access
   - Enable Event Subscription
   - Provide a subscription name and Event Notification URL
   - Choose an Authentication Header Option
   - Select Add Events
   - Search for "rtms" and select the RTMS Endpoints

5. **Configure Meeting Features**:
   - Navigate to Features → Surface
   - Select Meetings
   - [Optional] In the Home URL section, provide a URL to your app's home page
   - Add the URL to the Domain allow list
   - In the In-Client App Features, enable the Zoom App SDK
   - [Optional] Click on Add APIs and add "startRTMS" and "stopRTMS" API permissions

6. **Configure Scopes**:
   - Navigate to Scopes
   - Select Add Scopes
   - Search for "rtms"
   - Add the scopes for both "Meetings" and "Rtms"

7. **Complete Setup**:
   - Navigate to Add your app → Local Test
   - Select Add App now
   - Complete the Authorization Flow

8. **Get Your Credentials**:
   - After creating the app, you'll receive:
     - Client ID
     - Client Secret
     - Webhook verification token
   - Save these credentials securely - you'll need them for the samples

## Troubleshooting

1. **Connection Issues**:
   - Verify ngrok is running and the tunnel is active
   - Check your Zoom OAuth credentials in the `.env` file
   - Ensure your webhook URL is correctly configured

2. **SDK Installation Issues**:
   - Make sure you have the correct token for fetching prebuilt binaries
   - Check that you've installed the SDK correctly: `npm install github:zoom/rtms`

3. **No Audio Data**:
   - Verify that Auto-Start is enabled for your app in Zoom web settings
   - Check that your app has the correct RTMS scopes
   - Ensure you're properly handling the `meeting.rtms_started` webhook event

4. **WAV Conversion Issues**:
   - Verify FFmpeg is installed and accessible in your PATH
   - RTMS sends uncompressed raw audio data (L16 PCM) at 16kHz sample rate, mono channel
   - Use the correct FFmpeg parameters: `-f s16le -ar 16000 -ac 1`

## License

This project is licensed under the MIT License.

Copyright (c) 2025 Zoom Video Communications, Inc.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE. 