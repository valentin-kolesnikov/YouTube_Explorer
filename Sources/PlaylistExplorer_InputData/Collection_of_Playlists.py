from ForthFunctions.collecting_info import collect_other_playlists, collect_playlist_details #, collect_your_playlists

from ForthFunctions.output import output_playlists

from Patterns.Search_Engine import search_engine




def collection_of_playlists(youtube, exc_OAuth2):
    while True:
        print("\n1. Other's playlists")

        if not exc_OAuth2:
            print("2. Your playlists")

        search_playlist = input("\nChoose the number: ")

        if search_playlist == "1":
            
            keywords, ageAfter, ageBefore, _, maximum, which_order, _ = search_engine(playlist_enabled=True)

            playlist_ids, exc = collect_other_playlists(youtube, keywords, ageAfter, ageBefore, maximum, which_order)
            if exc:
                print("\033[H\033[J", end="")
                return
            
            statrequest = collect_playlist_details(youtube, playlist_ids)
            
            print("\033[H\033[J", end="")

            output_playlists(statrequest)
            
            input("\nPress Enter to return...")

            print("\033[H\033[J", end="")
            return
        


        
        
        #soon
        
        # elif search_playlist == "2" and not exc_OAuth2:
        #     collect_your_playlists(youtube)
        # OAuth needed  playlistItems.list() - поиск по плейлисту 
        # playlists.list() - для нахождения имен имеющихся плейлистов playlist_id = input("Enter the playlist's URL: ")

        # else:
        #     search_playlist = input("Enter again: ")