"""
CLI Utilities Module

This module contains utility functions for command-line interface operations.
Provides functions for screen clearing and other terminal manipulations.

Functions:
- clear_screen(): Clear the terminal screen
"""

import os


def clear_screen():
    """
    Clear the terminal screen using ANSI escape codes.

    Uses ANSI escape sequences that work across different platforms
    including Windows Terminal, PowerShell, macOS, and Linux terminals.
    """
    # ANSI escape code to clear screen and move cursor to top-left
    print('\033[2J\033[1;1H', end='')
    