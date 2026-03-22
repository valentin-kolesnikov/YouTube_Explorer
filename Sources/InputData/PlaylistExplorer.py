from re import search







def start_extension(exc_OAuth2):
    print("\n1. Collecting playlists\n" \
    "2. Collecting videos from the playlist")

    if not exc_OAuth2:
        print("3. Collecting private playlists\n" \
        "4. Collecting liked videos playlist\n" \
        "5. Collecting watch later playlist")
    print("0. Go back to the start menu")

    question = input("\nChoose the number: ")
    
    return question






def playlist_URL_extract():
    playlist_URL = input("Enter the playlist URL with PL (possible separately): ")
    
    while True:
        playlist_URL = playlist_URL.strip()
        for_id = search(r"(PL[\w-]{32})", playlist_URL)
        if for_id:
            return for_id.group(1)

        playlist_URL = input("\nEnter again: ")




def filter_playlist_videos():
    amount = input("Enter the amount of videos to collect: ")

    while True:
        if amount.isdigit() and 0 < int(amount):
            amount = 1
            break
        
        else:
            amount = input("\nEnter again: ")

    return amount

