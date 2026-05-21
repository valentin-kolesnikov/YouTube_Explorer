from Modes.YouTubeCommentExplorer import launcherComments
from Modes.YouTubeVideoExplorer import launcherVideos
from Modes.YouTubeChannelExplorer import launcherChannels
from Modes.YouTubePlaylistExplorer import launcherPlaylists
from Modes.YouTubeSubtitlesExplorer import launcherSubtitles
from Modes.YouTubeOneVideoExplorer import launcherInfo
from Modes.YouTubeExplorerLicense import launcherABOUT, launcherLICENSE
from Modes.YouTubeASCIIExplorer import launcherASCII

from Starter.KeyExplorer import youtube_api_key, window_title, launcherKey
from Starter.QuotaExplorer import test_quota
from Starter.OAuth2 import youtube_OAuth2

from sys import exit









if __name__ == "__main__":
    window_title("YouTube Explorer")

    youtube, exc_OAuth2 = youtube_OAuth2()
    if exc_OAuth2:
        youtube = youtube_api_key()

    if not test_quota(youtube):
        input("\nPress Enter to exit...")
        exit(1)

    while True:             
        try:
            current_page = 1
            while True:
                print("\033[H\033[J", end="")
                print("==========  v1.2.0  ==========")

                if current_page == 1:
                    print(f"Page {current_page}\n")

                    questionist1 = input(
                        "1. Comments\n" \
                        "2. Videos\n" \
                        "3. Channels\n" \
                        "4. Playlists\n" \
                        "5. Subtitles\n" \
                        "6. One Video Info\n\n" \
                        "7. The next page...\n\n" \
                        "0. Exit\n\n" \
                        "Enter the number: "
                    )
                    
                    print("\033[H\033[J", end="")
                    
                    if questionist1 == "1":
                        launcherComments(youtube)
                    elif questionist1 == "2":
                        launcherVideos(youtube)
                    elif questionist1 == "3":
                        launcherChannels(youtube)
                    elif questionist1 == "4":
                        launcherPlaylists(youtube, exc_OAuth2) 
                    elif questionist1 == "5":
                        launcherSubtitles()
                    elif questionist1 == "6":
                        launcherInfo(youtube)
                    elif questionist1 == "7":
                        current_page = 2
                    elif questionist1 == "0":
                        exit(0)
                    else:
                        questionist1 = input("\nEnter again: ")
                            
                elif current_page == 2:
                    print(f"Page {current_page}\n")

                    questionist2 = input(
                        "1. YouTube API Key\n" \
                        "2. ASCII Art\n" \
                        "3. LICENSE\n" \
                        "4. ABOUT\n\n" \
                        "7. The previous page...\n\n" \
                        "0. Exit\n\n" \
                        "Enter the number: "
                    )
                    
                    print("\033[H\033[J", end="")
                    
                    if questionist2 == "1":
                        launcherKey(exc_OAuth2)
                    elif questionist2 == "2":
                        launcherASCII()
                    elif questionist2 == "3":
                        launcherLICENSE()
                    elif questionist2 == "4":
                        launcherABOUT()
                    elif questionist2 == "7":
                        break
                    elif questionist2 == "0":
                        exit(0)
                    else:
                        questionist2 = input("\nEnter again: ")

        except KeyboardInterrupt:
            pass