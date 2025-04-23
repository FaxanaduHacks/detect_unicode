"""
detect_unicode.py

This program scans a text file and reports all non-ASCII (Unicode) characters,
including emojis, accented characters, invisible characters, symbols, and
non-Latin scripts. The program displays the character, its Unicode code point,
its official name, and its position (line and column) in the file.

Usage:
    python detect_unicode.py <file_path>
"""

import sys
import os
import unicodedata

# ANSI escape codes for terminal color formatting:
WHITE = '\033[97m'
CYAN = '\033[96m'
MAGENTA = '\033[95m'
VIOLET = '\033[38;5;135m'
RED = '\033[91m'
RESET = '\033[0m'

def get_unicode_info(char):
    """
    Returns the Unicode code point and official name for a given character.

    Args:
        char (str): A single Unicode character.

    Returns:
        str: Formatted string with Unicode code and name.
    """
    code = f"U+{ord(char):04X}"
    try:
        name = unicodedata.name(char)
    except ValueError:
        name = "UNKNOWN CHARACTER"
    return f"{code} ({name})"

def detect_unicode_chars(file_path):
    """
    Detects and prints all non-ASCII (Unicode) characters in a text file,
    including their position and Unicode metadata.

    Args:
        file_path (str): Path to the file to be scanned.
    """
    if not os.path.isfile(file_path):
        print(f"{RED}Error: File {WHITE}'{file_path}'{RED} does not exist.{RESET}")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    total_found = 0
    print(f"{WHITE}Scanning file: {RED}{file_path}{RESET}\n")

    for lineno, line in enumerate(lines, start=1):
        for col, char in enumerate(line, start=1):
            if ord(char) > 127:
                info = get_unicode_info(char)
                print(f"{WHITE}Line {MAGENTA}{lineno}{WHITE}, Col {CYAN}{col}{WHITE}: {repr(char)} -> {VIOLET}{info}{RESET}")
                total_found += 1

    if total_found == 0:
        print(f"\n{WHITE}No Unicode characters found.{RESET}")
    else:
        print(f"\n{WHITE}Total Unicode characters found: {MAGENTA}{total_found}{RESET}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python detect_unicode.py <file_path>")
    else:
        detect_unicode_chars(sys.argv[1])
