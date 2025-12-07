from googleapiclient.errors import HttpError

from Patterns.errors import http_error, WinError

def channel_search(youtube, video_id):
    try:
        request = youtube.search().list(
            part="snippet",
            videoId=video_id,
            type="video"
    ).execute()

        for item in request["items"]:
            channel = item["snippet"]["channelId"]

        return channel, False
        
        
    except HttpError as exc:
        
        http_error(exc)
        
        return {}, True
    
    
    except OSError as exc:

        WinError(exc)

        return {}, True