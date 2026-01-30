import os

import sys



if getattr(sys, "frozen", False):
    dir = os.path.dirname(os.path.dirname(sys.executable))
else:
    dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))





def launcherLICENSE():
    license = os.path.join(dir, "LICENSE")

    if os.path.isfile(license):
        with open(license, "r", encoding="utf-8") as f:
            license_text = f.read()

    else:
        input("The LICENSE file was not found.\n" \
        "This software is distributed under the Apache 2.0 License.\n" \
        "Original project repository: https://github.com/valentin-kolesnikov/YouTube_Explorer\n\n" \
        "Original project: YouTube Explorer by Valentin Kolesnikov\n\n" \
        "Press Enter to return...")

        return

    os.system('cls')

    print(license_text)

    input("Press Enter to return...")






def launcherNOTICE():
    notice = os.path.join(dir, "NOTICE")

    if os.path.isfile(notice):
        with open(notice, "r", encoding="utf-8") as f:
            notice_text = f.read()

    else:
        input("The NOTICE file was not found.\n" \
        "This software is distributed under the Apache 2.0 License.\n" \
        "Original project repository: https://github.com/valentin-kolesnikov/YouTube_Explorer\n\n" \
        "Original project: YouTube Explorer by Valentin Kolesnikov\n\n" \
        "Press Enter to return...")

        return
    
    os.system('cls')

    print(notice_text)

    input("Press Enter to return...")