"""One line about a small good thing that happened today.

Writes the entry to /output/entry.txt (UTF-8, 1-200 characters, one line).
"""

import os

ENTRY = "My neighbour left three warm tomatoes on my doorstep with a note: 'From the plant you gave me - don't argue.'"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
