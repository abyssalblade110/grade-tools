"""
Highest Number Finder

A simple utility for finding the highest value among three numbers.

Author: Abyssalblade110
Version: 1.0.0
"""
import os
import time
from typing import Union, Tuple


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
    'BG_YELLOW': '\033[43m',
    'BG_BLUE': '\033[44m',
    'BG_RED': '\033[41m'
}

# Grade thresholds and corresponding styles
GRADE_INFO = {
    'A': {'range': (90, 100), 'color': COLORS['GREEN'], 'description': 'Excellent'},
    'B': {'range': (80, 89), 'color': COLORS['BLUE'], 'description': 'Good'},
    'C': {'range': (70, 79), 'color': COLORS['YELLOW'], 'description': 'Satisfactory'},
    'D': {'range': (60, 69), 'color': COLORS['MAGENTA'], 'description': 'Needs Improvement'},
    'F': {'range': (0, 59), 'color': COLORS['RED'], 'description': 'Failing'}
}


def clear_screen() -> None:
    """Clear the terminal screen in a cross-platform way."""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_header() -> None:
    """Display an attractive header for the application."""
    header = f"""
    {COLORS['BOLD']}{COLORS['CYAN']}╔═══════════════════════════════════════╗
    ║       GRADE CONVERSION SYSTEM       ║
    ╚═══════════════════════════════════════╝{COLORS['RESET']}
    """
    print(header)


def print_grade_scale() -> None:
    """Display the grade scale information."""
    print(f"\n{COLORS['BOLD']}Grade Scale:{COLORS['RESET']}")
    for grade, info in GRADE_INFO.items():
        min_score, max_score = info['range']
        print(f"  {info['color']}{grade}{COLORS['RESET']}: {min_score}-{max_score} - {info['description']}")
    print()


def convert_grade(score: float) -> Tuple[str, str, str]:
    """Convert a numerical score to a letter grade with styling.

    Args:
        score: The numerical score to convert (0-100)

    Returns:
        Tuple containing the letter grade, color code, and description
    """
    for grade, info in GRADE_INFO.items():
        min_score, max_score = info['range']
        if min_score <= score <= max_score:
            return grade, info['color'], info['description']

    return 'Invalid', COLORS['RED'], 'Score out of range'


def get_valid_score() -> Union[float, None]:
    """Get and validate a score input from the user.

    Returns:
        A valid score or None if the input was invalid
    """
    try:
        score_input = input(f"\n{COLORS['CYAN']}Enter the grade (0-100): {COLORS['RESET']}")
        score = float(score_input)

        if 0 <= score <= 100:
            return score
        else:
            print(f"\n{COLORS['RED']}Error: Score must be between 0 and 100.{COLORS['RESET']}")
            return None
    except ValueError:
        print(f"\n{COLORS['RED']}Error: Please enter a valid number.{COLORS['RESET']}")
        return None


def display_result(score: float, grade: str, color: str, description: str) -> None:
    """Display the grade conversion result with visual styling.

    Args:
        score: The numerical score
        grade: The letter grade
        color: ANSI color code for the grade
        description: Description of the grade
    """
    result = f"""
    {COLORS['BOLD']}Result:{COLORS['RESET']}
    ┌───────────────────────────────────┐
    │  Score: {score:<27} │
    │  Grade: {color}{grade}{COLORS['RESET']}{' ' * 27} │
    │  Assessment: {description:<20} │
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
        print_grade_scale()

        score = get_valid_score()
        if score is None:
            return

        # Add a small delay for effect
        print(f"\n{COLORS['CYAN']}Converting...{COLORS['RESET']}")
        time.sleep(0.5)

        # Convert and display the letter grade
        grade, color, description = convert_grade(score)
        display_result(score, grade, color, description)

        print(f"\n{COLORS['CYAN']}Thank you for using the Grade Conversion System!{COLORS['RESET']}")

    except KeyboardInterrupt:
        print(f"\n\n{COLORS['YELLOW']}Program terminated by user.{COLORS['RESET']}")
    except Exception as e:
        print(f"\n{COLORS['RED']}An unexpected error occurred: {str(e)}{COLORS['RESET']}")


if __name__ == "__main__":
    main()
