from googleapiclient.errors import HttpError

from Patterns.errors import http_error, WinError








def collect_stats(youtube, video_ids):
    try:
        statrequest = []

        for i in range(0, len(video_ids), 50):

            statrequest_videos = youtube.videos().list(
                part="snippet,statistics",
                id=",".join(video_ids[i:i+50])
            ).execute()

            statrequest.extend(statrequest_videos["items"])

        return statrequest, False
    
    
    except HttpError as exc:

        http_error(exc)

        return {}, True
    
    except OSError as exc:

        WinError(exc)

        return {}, True
    
    except Exception:
        
        print("Probably, YouTube has problems with submitted objects")

        return {}, True
        

    