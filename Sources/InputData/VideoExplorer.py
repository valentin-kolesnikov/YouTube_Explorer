from Patterns.Search_Engine import search_engine

from re import fullmatch





def searching_for_videos():
    region = input("What region would you like? (Enter as US, RU, UK, etc): ").upper()
    while True:      
        if not region.isalpha():
            region = input("\nEnter it again in letters: ").upper()

        elif len(region) != 2:
            region = input("\nEnter again: ").upper()

        elif not fullmatch(r"[A-Za-z]+", region):
            region = input("\nEnter it again in English: ").upper()

        elif len(region) == 2 and region.isalpha():
            break

        



    keywords, ageAfter, ageBefore, duration, maximum, which_order, dimension = search_engine(playlist_enabled=False)


    return keywords, region, ageAfter, ageBefore, duration, maximum, which_order, dimension