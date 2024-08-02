# The CLIENT_SECRET_FILE should be the file you downloaded from Google Developers Console
CLIENT_SECRET_FILE = 'client_secret.json'

import os
import time
import google.auth.transport.requests
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Scopes for YouTube Data API
SCOPES = ['https://www.googleapis.com/auth/youtube.readonly']

def get_authenticated_service():
    """Authenticates and constructs the YouTube API service."""
    # Check if there are existing credentials
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    # If there are no valid credentials available, request login
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(google.auth.transport.requests.Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CLIENT_SECRET_FILE, SCOPES)
            
            # Use a local server with the correct redirect URI
            creds = flow.run_local_server(port=8000)

        # Save the credentials for the next run
        with open('token.json', 'w') as token_file:
            token_file.write(creds.to_json())

    return build('youtube', 'v3', credentials=creds)

def get_channel_statistics(youtube, channel_id):
    """Fetches the statistics for a given YouTube channel, including view count and subscriber count."""
    try:
        request = youtube.channels().list(
            part="statistics",
            id=channel_id
        )
        response = request.execute()

        # Print the entire response for debugging
        print("API Response:", response)

        # Check if 'items' is in the response
        if 'items' in response and len(response['items']) > 0:
            stats = response["items"][0]["statistics"]
            view_count = stats.get("viewCount", "N/A")
            subscriber_count = stats.get("subscriberCount", "N/A")
            return view_count, subscriber_count
        else:
            print("No data found for the given channel ID.")
            return None, None

    except Exception as e:
        print("An error occurred:", e)
        return None, None

def main():
    # Authenticate and construct the YouTube service
    youtube = get_authenticated_service()
    
    # Replace with the actual channel ID you want to query
    channel_id = 'UCUr0nT91YLMe7QyKkxr1eNA'  # Example channel ID
    
    while True:
        # Fetch and print the channel statistics
        view_count, subscriber_count = get_channel_statistics(youtube, channel_id)
        if view_count is not None and subscriber_count is not None:
            print(f"Channel Views: {view_count}")
            print(f"Channel Subscribers: {subscriber_count}")
        else:
            print("Unable to fetch statistics for the channel.")

        # Wait for 9 seconds before the next request to respect quota limits
        time.sleep(10)

if __name__ == '__main__':
    main()