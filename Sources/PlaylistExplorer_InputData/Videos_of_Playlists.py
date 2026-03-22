from Patterns.collectingStats import collect_stats

from ForthFunctions.collecting_info import collect_videos_of_playlist

from InputData.PlaylistExplorer import filter_playlist_videos, playlist_URL_extract





def videos_of_playlists(youtube):
    playlist_URL = playlist_URL_extract()

    amount = filter_playlist_videos()

    video_ids = collect_videos_of_playlist(youtube, playlist_URL, amount)

    collect_stats(youtube, video_ids) 




    input("\nPress Enter to return...")

    print("\033[H\033[J", end="")
    return