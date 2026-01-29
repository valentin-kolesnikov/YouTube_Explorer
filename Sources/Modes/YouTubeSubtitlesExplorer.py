from youtube_transcript_api import YouTubeTranscriptApi

from youtube_transcript_api._errors import (VideoUnplayable, RequestBlocked, TranscriptsDisabled)

from Patterns.EnteringURL import youtube_id_finder

from FifthFunctions.collecting_info import transcript_fetcher

from FifthFunctions.output import available_languages, transcript_fetch, output

from InputData.SubtitlesExplorer import *

import os







def launcherSubtitles(youtube):
    video_id = youtube_id_finder()
    try:
        video_list = YouTubeTranscriptApi().list(video_id)
    
    except VideoUnplayable:

        input("\nERROR: the video is unplayable\n\nPress Enter to return...")

        return
    
    except RequestBlocked:

        input("\nERROR: YouTube is blocking requests from your IP\n\nPress Enter to return...")

        return
    
    except TranscriptsDisabled:

        input("\nERROR: the video does not have subtitles\n\nPress Enter to return...")

        return
    

    languages_list = language_needed()

    manually_generated = view_of_text()

    transcript_subtitles, exc = transcript_fetcher(video_list, languages_list, manually_generated)
    if exc:
        os.system('cls')
        return
    
    available_lang = available_languages(transcript_subtitles)

    full_text = transcript_fetch(transcript_subtitles)

    os.system('cls')

    output(transcript_subtitles, available_lang, full_text)

    input("\nPress Enter to return...")