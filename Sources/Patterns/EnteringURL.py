import re






def youtube_id_finder():
    url = input("\nEnter the url: ")

    while True:
        pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11})"
        match = re.search(pattern, url)

        if match:
            return match.group(1)
        
        else:
            url = input("\nTry entering the url again: ")