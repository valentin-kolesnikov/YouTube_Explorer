from datetime import datetime
from json import dump 
from pathlib import Path



class HistorySessions:
    def __init__(self, tool):

        self.tool = tool

        now = datetime.now()

        self.timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")

        self.created_at = now.strftime("%Y-%m-%d %H:%M:%S")

        self.folder = Path("YouTubeHistory", 
                            now.strftime("%Y"),
                            now.strftime("%m"),
                            now.strftime("%d"))
        
        self.folder.mkdir(parents=True, exist_ok=True)

        self.file = f"{self.timestamp}_{tool}.json"

        self.path = self.folder / self.file

        self.data = {
            "actions": self.now(),
            "tool": tool,
            "sessions": []
        }
    
    def now(self):
        return datetime.now().strftime("%H:%M:%S")

    def add_session(self, action, **data):

        self.data["sessions"].append({
            "time": self.now(),
            "action": action,
            "data": data
        })
        
    def save(self):
        with open(self.path, "w", encoding="utf-8") as files:
            dump(self.data, files, ensure_ascii=False, indent=4)