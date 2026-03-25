from Patterns.collectingStats import collect_stats

from Patterns.asyncRYD import ryd

from SecondFunctions.output import output_videos

from ForthFunctions.collecting_info import collect_videos_of_playlist

from InputData.PlaylistExplorer import playlist_URL_extract

from asyncio import run






def videos_of_playlists(youtube):
    playlist_URL = playlist_URL_extract()

    video_ids, exc = collect_videos_of_playlist(youtube, playlist_URL)
    if exc:
        print("\033[H\033[J", end="")
        return
    
    results = run(ryd(video_ids))

    statrequest, exc = collect_stats(youtube, video_ids)
    if exc:
        print("\033[H\033[J", end="")
        return

    print("\033[H\033[J", end="")

    print(f"https://www.youtube.com/playlist?list={playlist_URL}\n")
    output_videos(results, statrequest)

    input("\nPress Enter to return...")
    return