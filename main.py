#!/usr/bin/env python3
"""Write the one-line smile to /output/entry.txt.

One line, at most 200 characters, about a small good thing that
happened today.
"""
import os

TEXT = "This morning the bus driver held the bus while an old man counted his coins, one by one, then waved off the fare, and the whole bus clapped — and the old man bowed like he had just won something."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
