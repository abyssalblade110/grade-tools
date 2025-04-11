"""
Highest Number Finder

A simple utility for finding the highest value among three numbers.

Author: Abyssalblade110
Version: 1.0.0
"""

import os
import time
from typing import Union, List


# ANSI color codes for terminal styling
COLORS = {
    'RESET': '\033[0m',
    'BOLD': '\033[1m',
    'GREEN': '\033[32m',
    'YELLOW': '\033[33m',
    'BLUE': '\033[34m',
    'MAGENTA': '\033[35m',
    'CYAN': '\033[36m',
    'RED': '\033[31m',
    'BG_GREEN': '\033[42m',
    'BG_BLUE': '\033[44m'
}


def clear_screen() -> None:
    """Clear the terminal screen in a cross-platform way."""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_header() -> None:
    """Display an attractive header for the application."""
    header = f"""
    {COLORS['BOLD']}{COLORS['BLUE']}╔═══════════════════════════════════════╗
    ║     HIGHEST NUMBER FINDER SYSTEM     ║
    ╚═══════════════════════════════════════╝{COLORS['RESET']}
    """
    print(header)


def find_highest(numbers: List[float]) -> float:
    """Find the highest number in a list.

    Args:
        numbers: List of numbers to compare

    Returns:
        The highest number in the list
    """
    return max(numbers)


def get_valid_number(prompt: str) -> Union[float, None]:
    """Get and validate a number input from the user.

    Args:
        prompt: The prompt message to display

    Returns:
        A valid number or None if the input was invalid
    """
    try:
        number_input = input(f"{COLORS['CYAN']}{prompt}: {COLORS['RESET']}")
        return float(number_input)
    except ValueError:
        print(f"\n{COLORS['RED']}Error: Please enter a valid number.{COLORS['RESET']}")
        return None


def collect_numbers() -> Union[List[float], None]:
    """Collect three numbers from the user.

    Returns:
        A list of three valid numbers or None if any input was invalid
    """
    print(f"\n{COLORS['BOLD']}Enter three numbers to find the highest:{COLORS['RESET']}")

    numbers = []
    prompts = ["Enter first number", "Enter second number", "Enter third number"]

    for prompt in prompts:
        number = get_valid_number(prompt)
        if number is None:
            return None
        numbers.append(number)

    return numbers


def display_result(numbers: List[float], highest: float) -> None:
    """Display the result with visual styling.

    Args:
        numbers: The list of input numbers
        highest: The highest number found
    """
    # Create a visual representation of the numbers
    bars = []
    max_bar_length = 20
    max_num = max(abs(n) for n in numbers)

    for num in numbers:
        # Scale the bar length relative to the highest absolute value
        if max_num != 0:  # Avoid division by zero
            bar_length = int((abs(num) / max_num) * max_bar_length)
        else:
            bar_length = 0

        # Choose color based on whether this is the highest number
        color = COLORS['BG_GREEN'] if num == highest else COLORS['BG_BLUE']
        bar = f"{color}{' ' * bar_length}{COLORS['RESET']}"
        bars.append(bar)

    result = f"""
    {COLORS['BOLD']}Result:{COLORS['RESET']}
    ┌───────────────────────────────────┐
    │  Number 1: {numbers[0]:<10} {bars[0]} │
    │  Number 2: {numbers[1]:<10} {bars[1]} │
    │  Number 3: {numbers[2]:<10} {bars[2]} │
    ├───────────────────────────────────┤
    │  {COLORS['BOLD']}Highest: {COLORS['GREEN']}{highest}{COLORS['RESET']}{' ' * 22} │
    └───────────────────────────────────┘
    """

    # Add animation effect
    for line in result.split('\n'):
        print(line)
        time.sleep(0.1)


def main() -> None:
    """Main application function."""
    try:
        clear_screen()
        print_header()

        numbers = collect_numbers()
        if numbers is None:
            return

        # Add a small delay for effect
        print(f"\n{COLORS['CYAN']}Calculating...{COLORS['RESET']}")
        time.sleep(0.5)

        # Find and display the highest number
        highest = find_highest(numbers)
        display_result(numbers, highest)

        print(f"\n{COLORS['CYAN']}Thank you for using the Highest Number Finder!{COLORS['RESET']}")

    except KeyboardInterrupt:
        print(f"\n\n{COLORS['YELLOW']}Program terminated by user.{COLORS['RESET']}")
    except Exception as e:
        print(f"\n{COLORS['RED']}An unexpected error occurred: {str(e)}{COLORS['RESET']}")


if __name__ == "__main__":
    main()
