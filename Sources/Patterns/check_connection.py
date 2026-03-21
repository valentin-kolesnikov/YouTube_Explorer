from Patterns.errors import WinError

from urllib.request import urlopen






def internet_available():
    try:
        urlopen("https://google.com", timeout=3)
        return True

    except OSError as exc:
        
        WinError(exc)