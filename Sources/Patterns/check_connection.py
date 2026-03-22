from Patterns.errors import WinError

from urllib.request import urlopen






def internet_available():
    while True:
        try:
            urlopen("http://clients3.google.com/generate_204", timeout=3)
            return True

        except OSError as exc:
            
            WinError(exc)