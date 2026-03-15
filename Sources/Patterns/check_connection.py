from Patterns.errors import WinError

import urllib.request






def internet_available():
    try:
        urllib.request.urlopen("https://google.com", timeout=3)
        return True

    except OSError as exc:
        
        WinError(exc)