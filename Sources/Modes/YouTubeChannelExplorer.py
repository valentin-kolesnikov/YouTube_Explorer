from InputData.ChannelExplorer import get_info, get_answer

from ThirdFunctions.collecting_info import collect_channel_info, search_channel_videos, collect_popular_videos

from ThirdFunctions.output import output_channel_info

from Patterns.Search_Engine import search_engine

from Patterns.check_connection import internet_available

from Patterns.collectingStats import collect_stats

from Patterns.asyncRYD import ryd

from asyncio import run







def launcherChannels(youtube):
    for_id, for_handle = get_info()

    get_answers = get_answer()

    snistics, uploads_videos, exc = collect_channel_info(youtube, for_id, for_handle)
    if exc:
        print("\033[H\033[J", end="")
        return
    
    if get_answers == "y":

        keywords, ageAfter, ageBefore, duration, maximum, which_order, dimension = search_engine(playlist_enabled=False)

        internet_available()

        video_ids, exc = search_channel_videos(youtube, snistics, keywords, ageAfter, ageBefore, duration, maximum, which_order, dimension)
        if exc:
            print("\033[H\033[J", end="")
            return
        
        result = run(ryd(video_ids))

        statrequests, exc = collect_stats(youtube, video_ids)
        if exc:
            print("\033[H\033[J", end="")
            return
        
        print("\033[H\033[J", end="")

        output_channel_info(result, statrequests, get_answers, snistics)




    elif get_answers == "n":

        internet_available()

        video_ids, exc = collect_popular_videos(youtube, uploads_videos)
        if exc:
            print("\033[H\033[J", end="")
            return

        result = run(ryd(video_ids))

        statrequests, exc = collect_stats(youtube, video_ids)
        if exc:
            print("\033[H\033[J", end="")
            return
        
        print("\033[H\033[J", end="")

        output_channel_info(result, statrequests, get_answers, snistics)

    input("\n\nPress Enter to return...")