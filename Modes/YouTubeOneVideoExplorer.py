from Patterns.asyncRYD import ryd

from Patterns.EnteringURL import youtube_id_finder

from Patterns.collectingStats import collect_stats

from Patterns.check_connection import internet_available

from SecondFunctions.output import output_videos

from asyncio import run





def launcherInfo(youtube):
    video_id = youtube_id_finder()

    internet_available()
    
    statrequest, exc = collect_stats(youtube, [video_id])
    if exc:
        print("\033[H\033[J", end="")
        return
    
    results = run(ryd([video_id]))

    print("\033[H\033[J", end="")

    output_videos(results, statrequest, one_video_info=True)

    input("\n\nPress Enter to return...")