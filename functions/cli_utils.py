import os


def clear_screen():
    # Use ANSI escape codes for cross-platform screen clearing
    # Works on Windows (Terminal/PowerShell), macOS, Linux, and most modern terminals
    print('\033[2J\033[1;1H', end='')
    