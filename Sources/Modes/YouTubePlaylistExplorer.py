from InputData.PlaylistExplorer import start_extension 

from PlaylistExplorer_InputData.Collection_of_Playlists import collection_of_playlists

from PlaylistExplorer_InputData.Liked_Videos import liked_videos

from PlaylistExplorer_InputData.Videos_of_Playlists import videos_of_playlists

from PlaylistExplorer_InputData.Videos_of_Private_Playlists import videos_of_private_playlists

from PlaylistExplorer_InputData.Watch_Later_Videos import watch_later_videos





def launcherPlaylists(youtube, exc_OAuth2):
    while True:
        question = start_extension(exc_OAuth2)
        if question == "0":
            return

        while True:
            if question == "1":
                print("\033[H\033[J", end="")
                collection_of_playlists(youtube, exc_OAuth2)
                break

            elif question == "2":
                print("\033[H\033[J", end="")
                videos_of_playlists(youtube)
                break

            elif question == "3" and not exc_OAuth2:
                print("\033[H\033[J", end="")
                videos_of_private_playlists(youtube)
                break

            elif question == "4" and not exc_OAuth2:
                print("\033[H\033[J", end="")
                liked_videos(youtube)
                break

            elif question == "5" and not exc_OAuth2:
                print("\033[H\033[J", end="")
                watch_later_videos(youtube)
                break
            
            else:
                question = input("Enter again: ")


        