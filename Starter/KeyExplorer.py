import sys
from pathlib import Path

from googleapiclient.discovery import build

from Patterns.save_history import clear
from Starter.QuotaExplorer import test_quota


def window_title(title):
    if sys.stdout.isatty():
        sys.stdout.write(f"\33]0;{title}\a")
        sys.stdout.flush()




if getattr(sys, "frozen", False):
    app_folder = Path(sys.executable).parent
else:
    app_folder = Path(__file__).parent


key_folder = Path(app_folder, "Keys")
key_folder.mkdir(parents=True, exist_ok=True)


key_file = Path(key_folder, "Key.bin")


class memory:

    def save_key(api_key):
        with open(key_file, "wb") as f:
            f.write(api_key.encode("utf-8"))


    def load_key():
        if key_file.exists():
            with open(key_file, "rb") as f:
                return f.read().decode("utf-8")
        return None



def youtube_api_key():
    api_key = memory.load_key()

    while api_key is None:
        if not api_key:
            api_key = input("Enter your YouTube API key: ").strip()

            while len(api_key) != 39:
                api_key = input("\nThis is not the YouTube API key. Try entering the API key again: ").strip()


        youtube = build('youtube', 'v3', developerKey=api_key, http=None)

        if not test_quota(youtube):
            re = input("\nThe API key is invalid or has exceeded its quota. Do you want to enter a new API key? (y/n): ").strip().lower()
            while re not in ["y", "n"]:
                re = input("\nInvalid input. Enter again (y/n): ").strip().lower()

            if re == "y":
                clear()
                api_key = None
                continue

            elif re == "n":
                sys.exit(0)


        choose = input("\n1. Use this API key\n2. Enter a new API key\n3. Exit\n\nChoose the number: ").strip()
        
        while True:
            if choose == "1":
                memory.save_key(api_key)
                return youtube
            elif choose == "2":
                clear()
                api_key = None
                break
            elif choose == "3":
                sys.exit(0)
            else:
                choose = input("\nInvalid number. Choose a valid number: ").strip()

    youtube = build('youtube', 'v3', developerKey=api_key, http=None) # proxy mode soon...

    return youtube