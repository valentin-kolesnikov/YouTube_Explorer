from PlaylistExplorer_InputData.Collection_of_Playlists import collection_of_playlists
from PlaylistExplorer_InputData.Videos_of_Playlists import videos_of_playlists





def launcherPlaylists(youtube, exc_OAuth2):
    question = input(
        "1. Collecting playlists\n" \
        "2. Collecting videos from the playlist\n" \
        "0. Go back to the start menu\n\n" \
        "Choose the number: "
        )
    
    while True:
        if question == "0":
            return
        
        elif question == "1":
            print("\033[H\033[J", end="")
            collection_of_playlists(youtube, exc_OAuth2)
            break

        elif question == "2":
            print("\033[H\033[J", end="")
            videos_of_playlists(youtube)
            break

        else:
            question = input("\nEnter again: ")