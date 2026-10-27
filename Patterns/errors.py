import sys
from json import JSONDecodeError, loads

from Patterns.color_output import red, reset


class PatternError:
    def pattern_exception(self, exc=None):
        if exc is None:
            return "Unexpected error occurred"
        
        print(f"\n{red}{type(exc).__name__}: {exc}{reset}")
        input("\nPress Enter to continue...")
        return str(exc)


def decode_error(exc):
    try:
        return loads(exc.content.decode("utf-8"))["error"]["errors"][0]["reason"]
    except KeyError, TypeError, IndexError, AttributeError, UnicodeDecodeError, JSONDecodeError:
        return None


def http_error(exc):
    status = exc.resp.status

    match status:
        case 400:
            issue = "Bad Request. There are some issues with Google requests. Make sure that you entered correctly."

        case 403:
            reason = decode_error(exc)

            if reason == "commentsDisabled":
                issue = "Forbidden. Comments of the video are disabled."

            elif reason == "quotaExceeded":
                print(f"\n\u001b[31mError {status}: Forbidden. You exceeded your YouTube API quota.\u001b[0m")

            else:
                issue = "Forbidden." + f"Reason: {reason}." if reason else ""
                
        case 404:
            issue = "Not Found. Probably, the requested video does not exist."

        case 429:
            issue = "Too Many Requests. You exceeded your Search Queries quota."

        case _:
            issue = exc.resp.reason

    print(f"\n{red}Error {status}: {issue}{reset}")
    

    input("\nPress Enter to continue...")

    return issue






def WinError(exc):

    match exc.errno:
        case 10054:
            issue = "Connection was forcibly closed by the remote host (WinError 10054)."

        case 10061:
            issue = "Connection refused (WinError 10061). Advice: try to turn off or configure the proxy correctly if you use one."

        case 11001:
            issue = "No Internet connection available (WinError 11001)."

        case _:
            issue = "Internet connection is probably unavailable."

    print(f"\n{red}{issue}{reset}")

    exit_continue = input(f"\n{red}1. Retry connection\n2. Exit\n\nYour choice: {reset}").strip()
    
    while True:
        if exit_continue == "1":
            return True
        
        elif exit_continue == "2":
            sys.exit(1)

        else:
            exit_continue = input(f"\n{red}Enter again: {reset}").strip()