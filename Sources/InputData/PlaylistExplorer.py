from re import search







def start_extension(exc_OAuth2):
    print("\033[H\033[J", end="")
    
    print("1. Collecting playlists\n" \
    "2. Collecting videos from the playlist")

    if not exc_OAuth2:
        print("3. Collecting private playlists")
    print("0. Go back to the start menu")

    question = input("\nChoose the number: ")
    
    return question






def playlist_URL_extract():
    playlist_URL = input('Enter the playlist URL with "PL" or "OL": ')
    
    while True:
        playlist_URL = playlist_URL.strip()
        for_id = search(r"(PL[\w-]{32})", playlist_URL)
        if for_id:
            return for_id.group(1)
        
        playlist_URL = playlist_URL.strip()
        for_id = search(r"(OL[\w-]{39})", playlist_URL)
        if for_id:
            return for_id.group(1)

        playlist_URL = input("\nEnter again: ")
