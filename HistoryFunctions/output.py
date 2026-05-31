from json import load



COMMENT_NAMES ={
    "video_link": "",
    "search_terms": "Keywords:",
    "which_order": "Order:",
    "status": "Status:",
    "error": "Error:",
    "amount_comments": "Total:",
    "file_path": "DOCX:",
    "counts": "Matches:"
}




def open_history_json(json_path, selected):
    with open(selected, "r", encoding="utf-8") as file:
        data = load(file)

    print(f"============ {json_path} ============\n")

    print(f"{data['tool']} Explorer")
    print(f"Time: {data['time']}\n")

    for session in data["sessions"]:
        print(f"\n{session['time_action']} | {session['action']}")
        if session["data"]:
            for key, value in session["data"].items():
                other_key = COMMENT_NAMES.get(key)

                if isinstance(value, dict):
                    print(f"    {other_key}")
                    for sub_key, sub_value in value.items():
                        print(f"        {sub_key}: {sub_value}")

                elif isinstance(value, list):
                    print(f"    {other_key}")
                    print(f"        {', '.join(value)}")

                else:
                    print(f"    {other_key} {value}")

    print("===================================================")

    
    exc = input('\n1. Main Menu\n2. Back\n\nEnter the number: ')
    while True:
        
        if exc == "1":
            return True
        elif exc == "2":
            return False
        else:
            exc = input('\nEnter it again correctly (1/2): ')