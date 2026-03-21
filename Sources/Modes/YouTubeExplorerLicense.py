from os import path

import sys





if getattr(sys, "frozen", False):
    dir = path.dirname(path.dirname(sys.executable))
else:
    dir = path.dirname(path.dirname(path.dirname(path.abspath(__file__))))


def launcherLICENSE():
    license = path.join(dir, "LICENSE")

    if path.isfile(license):
        with open(license, "r", encoding="utf-8") as f:
            license_text = f.read()

    else:
        input("The LICENSE file was not found.\n" \
        "This software is distributed under the Apache 2.0 License.\n" \
        "Original project repository: https://github.com/valentin-kolesnikov/YouTube_Explorer\n\n" \
        "Original project: YouTube Explorer by Valentin Kolesnikov\n\n" \
        "Press Enter to return...")

        return

    print("\033[H\033[J", end="")

    print(license_text)

    input("\nPress Enter to return...")




def launcherNOTICE():
    notice = path.join(dir, "NOTICE")

    if path.isfile(notice):
        with open(notice, "r", encoding="utf-8") as f:
            notice_text = f.read()

    else:
        input("The NOTICE file was not found.\n" \
        "This software is distributed under the Apache 2.0 License.\n" \
        "Original project repository: https://github.com/valentin-kolesnikov/YouTube_Explorer\n\n" \
        "Original project: YouTube Explorer by Valentin Kolesnikov\n\n" \
        "Press Enter to return...")

        return
    
    print("\033[H\033[J", end="")

    print(notice_text)

    input("\nPress Enter to return...")