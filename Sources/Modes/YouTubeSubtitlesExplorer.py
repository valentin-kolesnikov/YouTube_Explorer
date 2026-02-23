from youtube_transcript_api import YouTubeTranscriptApi

from youtube_transcript_api._errors import (VideoUnplayable, RequestBlocked, TranscriptsDisabled)

from Patterns.EnteringURL import youtube_id_finder

from FifthFunctions.collecting_info import transcript_fetcher

from FifthFunctions.output import available_languages, transcript_fetch, output

from InputData.SubtitlesExplorer import language_needed, view_of_text











def launcherSubtitles(youtube):
    video_id = youtube_id_finder()
    try:
        video_list = YouTubeTranscriptApi().list(video_id)
    
    except VideoUnplayable:

        input("\n\u001b[31mThe video is unplayable\u001b[0m\n\nPress Enter to return...")

        return
    
    except RequestBlocked:

        input("\n\u001b[31mYouTube is blocking requests from your IP\u001b[0m\n\nPress Enter to return...")

        return
    
    except TranscriptsDisabled:

        input("\n\u001b[31mThe video does not have subtitles\u001b[0m\n\nPress Enter to return...")

        return
    

    languages_list = language_needed()

    manually_generated = view_of_text()

    transcript_subtitles, exc = transcript_fetcher(video_list, languages_list, manually_generated)

    if exc:
        print("\033[H\033[J", end="")
        return
    
    available_lang = available_languages(transcript_subtitles)

    full_text = transcript_fetch(transcript_subtitles)

    print("\033[H\033[J", end="")

    output(transcript_subtitles, available_lang, full_text)

    input("\nPress Enter to return...")