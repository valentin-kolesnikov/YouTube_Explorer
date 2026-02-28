from Patterns.errors import WinError

import socket






def internet_available():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return
            
    except OSError as exc:
        
        WinError(exc)