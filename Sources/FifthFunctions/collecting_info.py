from youtube_transcript_api._errors import (NoTranscriptFound, 
                                             VideoUnavailable, 
                                             TranslationLanguageNotAvailable
                                             )



def transcript_fetcher(video_id_list, languages_list, manually_generated):
    try:
        if manually_generated == "1":
            transcript_subtitles = video_id_list.find_manually_created_transcript(languages_list)

        elif manually_generated == "2":
            transcript_subtitles = video_id_list.find_generated_transcript(languages_list)

        return transcript_subtitles, False
    
    except NoTranscriptFound:

        if manually_generated == "1":
            generated_forced = input("There is no manually created transcript. Do you need a generated transcript?\n\n" \
            "1. Yes\n2. No\n\nEnter the number: ")

            while True:

                if generated_forced == "1":
                    transcript_subtitles = video_id_list.find_generated_transcript(languages_list)
                    break

                elif generated_forced == "2":
                    return {}, True
                
                else:
                    generated_forced = input("Enter again: ")


        elif manually_generated == "2":

            manually_forced = input("There is no generated transcript. Do you need a manually created transcript?\n\n" \
            "1. Yes\n2. No\n\nEnter the number: ")

            while True:

                if manually_forced == "1":
                    transcript_subtitles = video_id_list.find_manually_created_transcript(languages_list)
                    break

                elif manually_forced == "2":
                    return {}, True
                
                else:
                    manually_forced = input("Enter again: ")
            

        return transcript_subtitles, False
    

    except NoTranscriptFound:

        input("No transcripts were found\n\nPress Enter to return...")

        return {}, True
    

    except VideoUnavailable:

        input("The video is unavailable\n\nPress Enter to return...")

        return {}, True
    
    except TranslationLanguageNotAvailable:

        input("The translation language is not available\n\nPress Enter to return...")

        return {}, True