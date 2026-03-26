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
        try:
            if manually_generated == "1":
                generated_forced = input("\nThere is no manually created transcript. Do you try to find a generated transcript?\n\n" \
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

                manually_forced = input("There is no generated transcript. Do you try to find a manually created transcript?\n\n" \
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

            input("\n\u001b[31mNo transcripts were found\u001b[0m\n\nPress Enter to return...")

            return {}, True
    

    except VideoUnavailable:

        input("\u001b[31mThe video is unavailable\u001b[0m\n\nPress Enter to return...")

        return {}, True
    
    except TranslationLanguageNotAvailable:

        input("\u001b[31mThe translation language is not available\u001b[0m\n\nPress Enter to return...")

        return {}, True
    
    except Exception:
        
        print("Probably, YouTube has problems with submitted objects")

        return {}, True