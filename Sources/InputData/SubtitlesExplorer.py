import re


def language_needed():
    languages = []
    language = input("\nEnter the desired language. Enter as (en; ru; ja...): ")

    while True:
        
        if len(language) != 2 and not re.fullmatch(r"[A-Za-z]+", language):
            language = input("\nEnter it again in English: ")
            continue

        if len(language) != 2:
            language = input("\nEnter again: ")
            continue

        if not re.fullmatch(r"[A-Za-z]+", language):
            language = input("\nEnter it again in English: ")
            continue

                
        languages.append(language.lower())

        language = input("\nEnter more if you want (Press Enter to continue): ")
        if language == "":
            break

    languages_list = list(dict.fromkeys(languages))

    return languages_list



def view_of_text():
    manually_generated = input("\n1. Manually created transcripts\n2. Generated transcripts\n\nEnter the number: ")

    while True:
        
        if manually_generated in ("1", "2"):
            break

        else:
            manually_generated = input("Enter again: ")
    
    return manually_generated