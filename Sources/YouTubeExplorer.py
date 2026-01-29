from Modes.YouTubeCommentExplorer import launcherComments

from Modes.YouTubeVideoExplorer import launcherVideos

from Modes.YouTubeChannelExplorer import launcherChannels

from Modes.YouTubePlaylistExplorer import launcherPlaylists

from Modes.YouTubeSubtitlesExplorer import launcherSubtitles

from Modes.YouTubeOneVideoInfoExplorer import launcherInfo

from Starter.KeyExplorer import youtube_api_key, window_title

from Starter.QuotaExplorer import test_quota

from Starter.OAuth2 import youtube_OAuth2

from sys import exit

import os







if __name__ == "__main__":
    while True:
        try:
            window_title("YouTube Explorer")

            youtube, exc_OAuth2 = youtube_OAuth2()
            if exc_OAuth2:

                youtube = youtube_api_key()

            if not test_quota(youtube):
                input("Press Enter to exit...")
                exit(1)

            while True:
                os.system('cls')
                print("=========  v.0.9.0  =========")

                questionist = input("1. Comments\n2. Videos\n3. Channels\n4. Playlists(still does not work)\n5. Subtitles\n6. Info of one video\n0. Exit\n\nEnter the number: ") 
                while True:
                    
                    if questionist == '1':
                        launcherComments(youtube)
                        break

                    elif questionist == '2':
                        launcherVideos(youtube)
                        break

                    elif questionist == '3':
                        launcherChannels(youtube)
                        break
                    
                    elif questionist == "4":
                        launcherPlaylists(youtube, exc_OAuth2)
                        break

                    elif questionist == '5':
                        launcherSubtitles(youtube)
                        break

                    elif questionist == "6":
                        launcherInfo(youtube)
                        break

                    elif questionist == '0':
                        exit(0)

                    else:
                        questionist = input("\nEnter again: ")

        except KeyboardInterrupt:
            pass