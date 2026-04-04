from googleapiclient.errors import HttpError

from Patterns.errors import http_error, WinError





def collect_searches(youtube, keywords, region, ageAfter, ageBefore, duration, maximum, which_order, dimension):
    try:
        video_ids = []
        next_page_token = None

        while True:
            remaining_results = maximum - len(video_ids)

            if remaining_results <= 0:
                break

            current_max_results = min(remaining_results, 50)

            request = youtube.search().list(
                videoDimension=dimension,
                q=keywords,
                regionCode=region,
                publishedBefore=ageBefore,
                order=which_order,
                publishedAfter=ageAfter,
                videoDuration=duration,
                part="snippet",
                type="video",
                maxResults=current_max_results,
                pageToken=next_page_token
            ).execute()

            
            for item in request["items"]:
                video_ids.append(item["id"]["videoId"])
            
            next_page_token = request.get("nextPageToken")

            if not next_page_token or len(video_ids) >= maximum:
                break

        return video_ids, False
    
    
    except HttpError as exc:
        
        http_error(exc)
        
        return {}, True
    
    
    except OSError as exc:

        WinError(exc)

        return {}, True
    
    except Exception:
        
        print("Probably, YouTube has problems with submitted objects")

        return {}, True