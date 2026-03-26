from ForthFunctions.collecting_info import collect_other_playlists, collect_playlist_details, collect_your_playlists

from PlaylistExplorer_InputData.Videos_of_Playlists import videos_of_playlists

from ForthFunctions.output import output_playlists

from Patterns.Search_Engine import search_engine










def videos_from_playlist(youtube):
    go_to_another_part = input("\n\nDo you want to analyze the certain playlist? (y/n): ")

    if go_to_another_part.lower() == "y":
        print("")
        videos_of_playlists(youtube)

    elif go_to_another_part.lower() == "n":
        return



def collection_of_playlists(youtube, exc_OAuth2):
    while True:
        print("1. Other's playlists")

        if not exc_OAuth2:
            print("2. Your playlists")

        search_playlist = input("\nChoose the number: ")

        if search_playlist == "1":
            
            keywords, ageAfter, ageBefore, _, maximum, which_order, _ = search_engine(playlist_enabled=True)

            playlist_ids, exc = collect_other_playlists(youtube, keywords, ageAfter, ageBefore, maximum, which_order)
            if exc:
                print("\033[H\033[J", end="")
                return
            
            statrequest, exc = collect_playlist_details(youtube, playlist_ids)
            if exc:
                print("\033[H\033[J", end="")
                return

            print("\033[H\033[J", end="")

            output_playlists(statrequest)
            
            videos_from_playlist(youtube)
            return
        

        elif search_playlist == "2" and not exc_OAuth2:
            statrequest, exc = collect_your_playlists(youtube)
            if exc:
                print("\033[H\033[J", end="")
                return

            print("\033[H\033[J", end="")

            output_playlists(statrequest)

            videos_from_playlist(youtube)
            return

    
        else:
            search_playlist = input("Enter again: ")


