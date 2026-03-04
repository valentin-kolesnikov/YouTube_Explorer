from Patterns.EnteringURL import youtube_id_finder

from InputData.CommentExplorer import youtube_filters

from FirstFunctions.collecting_info import collect_comments, channel_name

from FirstFunctions.output import count_keys, number_comments

from Patterns.check_connection import internet_available






def launcherComments(youtube):
    video_id = youtube_id_finder()

    which_order, search_terms = youtube_filters()

    internet_available()

    comments, exc = collect_comments(video_id, search_terms, which_order, youtube)
    if exc:
        print("\033[H\033[J", end="")
        return
    
    channel, exc = channel_name(video_id, youtube)
    if exc:
        print("\033[H\033[J", end="")
        return
    
    print("\033[H\033[J", end="")

    amount_comments = count_keys(comments, search_terms)
    if amount_comments == 0:
        input("\nPress Enter to return...")
        return

    number_comments(comments, channel)

    input("\nPress Enter to return...")