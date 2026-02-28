def http_error(exc):
    status = exc.resp.status

    if status == 400:
        print(f"\n\u001b[31mError {status}: Bad Request. There is some issues with Google requests.\u001b[0m")

    elif status == 403:
        print(f"\n\u001b[31mError {status}: Forbidden. Probably, you exceeded your YouTube API quota.\u001b[0m")

    elif status == 404:
        print(f"\n\u001b[31mError {status}: Not Found. Probably, the non-existent video was found.\u001b[0m")

    else:
        print(f"\n\u001b[31mUnexpected HTTP error: {status}\u001b[0m")
    
    input("\nPress Enter to return...")

def WinError(exc):
    
    if exc.errno == 10054:
        print("\n\u001b[31mConnection was forcibly closed by the remote host (WinError 10054)\u001b[0m")

    elif exc.errno == 11001:
        print("\n\u001b[31mNo Internet connection available (WinError 11001)\u001b[0m")

    else:
        print("\n\u001b[31mInternet connection is probably unavailable.\u001b[0m")

    exit_continue = input("\n\u001b[31m1. Retry connection\n2. Exit\n\nYour choice:\u001b[0m ")

    if exit_continue == "1":
        pass
    
    elif exit_continue == "2":
        exit(1)

    else:
        exit_continue = input("\u001b[31mEnter again:\u001b[0m ")