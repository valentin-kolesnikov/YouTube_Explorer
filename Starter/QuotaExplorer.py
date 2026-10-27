from googleapiclient.errors import HttpError
from httplib2.error import ServerNotFoundError

from Patterns.check_connection import internet_available
from Patterns.errors import PatternError, http_error


def test_quota(youtube):
    attempts = 0

    while True:
        try:
            youtube.channels().list(
                part="snippet",
                id="UC0PhYO05DXdztwxvRSDfSiw"
            ).execute()
            return True


        except HttpError as exc:
            http_error(exc)

            return False
        
        except ServerNotFoundError:
            attempts += 1

            if attempts >= 3:
                print("\nNo internet connection detected. Please check your connection and try again.")
                return False

            internet_available()

        except Exception as exc:
            PatternError().pattern_exception(exc)

            return False