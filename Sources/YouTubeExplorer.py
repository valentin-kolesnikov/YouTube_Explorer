from Modes.YouTubeCommentExplorer import launcherComments

from Modes.YouTubeVideoExplorer import launcherVideos

from Modes.YouTubeChannelExplorer import launcherChannels

from Modes.YouTubePlaylistExplorer import launcherPlaylists

from Modes.YouTubeSubtitlesExplorer import launcherSubtitles

from Modes.YouTubeOneVideoExplorer import launcherInfo

from Modes.YouTubeExplorerLicense import launcherNOTICE, launcherLICENSE

from Modes.YouTubeASCIIExplorer import launcherASCII

from Starter.KeyExplorer import youtube_api_key, window_title

from Starter.QuotaExplorer import test_quota

from Starter.OAuth2 import youtube_OAuth2

from sys import exit









if __name__ == "__main__":
    while True:
        try:
            window_title("YouTube Explorer")

            youtube, exc_OAuth2 = youtube_OAuth2()
            if exc_OAuth2:
                youtube = youtube_api_key()

            if not test_quota(youtube):
                input("\nPress Enter to exit...")
                exit(1)

            while True:
                print("\033[H\033[J", end="")
                print("==========  v1.0.0  ==========\n")

                questionist = input(
                    "1. Comments\n" \
                    "2. Videos\n" \
                    "3. Channels\n" \
                    "4. Playlists\n" \
                    "5. Subtitles\n" \
                    "6. One Video Info\n" \
                    "7. LICENSE\n" \
                    "8. NOTICE\n" \
                    # "9. ASCII Art" \
                    "0. Exit\n\n" \
                    "Enter the number: ")
                
                while True:
                    if questionist == "1":
                        print("\033[H\033[J", end="")
                        launcherComments(youtube)
                        break

                    elif questionist == "2":
                        print("\033[H\033[J", end="")
                        launcherVideos(youtube)
                        break

                    elif questionist == "3":
                        print("\033[H\033[J", end="")
                        launcherChannels(youtube)
                        break

                    elif questionist == "4":
                        print("\033[H\033[J", end="")
                        launcherPlaylists(youtube, exc_OAuth2) 
                        break

                    elif questionist == "5":
                        print("\033[H\033[J", end="")
                        launcherSubtitles(youtube)
                        break

                    elif questionist == "6":
                        print("\033[H\033[J", end="")
                        launcherInfo(youtube)
                        break

                    elif questionist == "7":
                        print("\033[H\033[J", end="")
                        launcherLICENSE()
                        break

                    elif questionist == "8":
                        print("\033[H\033[J", end="")
                        launcherNOTICE()
                        break

                    elif questionist == "9":
                        print("\033[H\033[J", end="")
                        launcherASCII()
                        break

                    elif questionist == "0":
                        exit(0)

                    else:
                        questionist = input("\nEnter again: ")

        except KeyboardInterrupt:
            pass