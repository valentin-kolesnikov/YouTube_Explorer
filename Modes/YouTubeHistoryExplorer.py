from HistoryFunctions.output import open_history_json

from pathlib import Path










def launcherHistory():
    
    try:
        json_path = Path("YouTubeHistory")
        while True:
        
            year_folders = sorted(json_path.iterdir(), key=lambda x: x.name)

            indexed = {}

            for index, folder in enumerate(year_folders, start=1):

                indexed[str(index)] = folder

                print(f"====== {json_path} ======\n")

                if folder.is_dir():
                    print(f"{index}. {folder.name}")

                else:
                    print(f"{index}. {folder.stem}")

            number = input("\nEnter the number of the year (Press Enter to return): ")

            if number == "":
                if json_path.name == "YouTubeHistory":
                    raise Exception

                json_path = json_path.parent
                print("\033[H\033[J", end="")
                continue
            
            selected = indexed.get(number)

            if not selected:
                print("\033[H\033[J", end="")
                continue

            if selected.is_dir():
                print("\033[H\033[J", end="")
                json_path = selected
                continue

            else:
                print("\033[H\033[J", end="")
                exc = open_history_json(json_path, selected)
                if exc:
                    raise Exception
                elif not exc:
                    print("\033[H\033[J", end="")
                    continue
                
            return selected, False

    except Exception:
        if not json_path.exists():
            print("\033[H\033[J", end="")
            print("No history found.")

            input("\nPress Enter to return...")
            return
        
        print("\033[H\033[J", end="")

        return