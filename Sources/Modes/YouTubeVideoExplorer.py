from InputData.VideoExplorer import searching_for_videos

from SecondFunctions.collecting_info import collect_searches

from Patterns.collectingStats import collect_stats

from SecondFunctions.output import output_videos

from Patterns.check_connection import internet_available

from Patterns.asyncRYD import ryd

import asyncio






def launcherVideos(youtube):
    keywords, region, ageAfter, ageBefore, duration, maximum, which_order, dimension = searching_for_videos()

    internet_available()
    
    video_ids, exc = collect_searches(youtube, keywords, region, ageAfter, ageBefore, duration, maximum, which_order, dimension)
    if exc:
        print("\033[H\033[J", end="")
        return

    results = asyncio.run(ryd(video_ids))

    statrequest, exc = collect_stats(youtube, video_ids)
    if exc:
        print("\033[H\033[J", end="")
        return
    
    print("\033[H\033[J", end="")

    output_videos(results, statrequest)

    input("\nPress Enter to return...")