from httplib2 import Http, HttpLib2Error

from Patterns.errors import WinError

TEST_URL = "https://youtube.googleapis.com/"

def internet_available():
    while True:
        try:
            Http(timeout=3).request(TEST_URL, "HEAD")
            return True
        except (OSError, HttpLib2Error):
            exc = OSError(11001, "No Internet connection available")
            
            if WinError(exc):
                continue