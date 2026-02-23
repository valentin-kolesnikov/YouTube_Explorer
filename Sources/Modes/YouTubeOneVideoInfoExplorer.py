from Patterns.asyncRYD import ryd

from Patterns.EnteringURL import youtube_id_finder

from Patterns.collectingStats import collect_stats

from SixthFunctions.output import output_info

import asyncio





def launcherInfo(youtube):
    video_id = youtube_id_finder()
    
    statrequest, exc = collect_stats(youtube, [video_id])
    if exc:
        print("\033[H\033[J", end="")
        return
    
    results = asyncio.run(ryd([video_id]))

    print("\033[H\033[J", end="")

    output_info(results, statrequest)

    input("Press Enter to return...")