"""
Vowel Counter - Level 2 Task
Counts the number of vowels in a given string
"""

# Simple color codes
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
MAGENTA = '\033[95m'
RESET = '\033[0m'

# Define vowels (both English and accented for completeness)
VOWELS = set('aeiouAEIOU')
# Include accented vowels for international text support
VOWELS_ACCENTED = set('áéíóúýàèìòùâêîôûäëïöüÿãõåæœ')

def count_vowels(text: str, include_accented: bool = True) -> int:
    """
    Count the number of vowels in a string.
    
    Args:
        text (str): The input string to analyze
        include_accented (bool): Whether to count accented vowels
        
    Returns:
        int: Number of vowels found
        
    Examples:
        >>> count_vowels("Hello World")
        3
        >>> count_vowels("Python Programming")
        4
    """
    if not text:  # Handle empty string
        return 0
    
    vowel_set = VOWELS
    if include_accented:
        vowel_set = VOWELS | VOWELS_ACCENTED
    
    # Count vowels using list comprehension
    vowel_count = sum(1 for char in text if char in vowel_set)
    
    return vowel_count

def get_vowel_details(text: str, include_accented: bool = True) -> dict:
    """
    Get detailed information about vowels in the string.
    
    Args:
        text (str): The input string to analyze
        include_accented (bool): Whether to include accented vowels
        
    Returns:
        dict: Dictionary with vowel counts and positions
    """
    vowel_set = VOWELS
    if include_accented:
        vowel_set = VOWELS | VOWELS_ACCENTED
    
    details = {
        'total_count': 0,
        'vowel_positions': [],
        'vowel_characters': []
    }
    
    for index, char in enumerate(text):
        if char in vowel_set:
            details['total_count'] += 1
            details['vowel_positions'].append(index)
            details['vowel_characters'].append(char)
    
    return details

def get_user_input() -> str:
    """
    Get user input for the string to analyze.
    
    Returns:
        str: User input string
    """
    while True:
        text = input(f"{CYAN}Enter a string to count vowels: {RESET}").strip()
        if text:  # Ensure non-empty input
            return text
        print(f"{RED}Please enter a non-empty string.{RESET}")

def main():
    """Main function to run the vowel counter."""
    print(f"{MAGENTA}{'='*50}{RESET}")
    print(f"{MAGENTA}VOWEL COUNTER".center(50))
    print(f"{MAGENTA}{'='*50}{RESET}")
    print("This program counts vowels (A, E, I, O, U) in a string.\n")
    
    # Get user input
    text = get_user_input()
    
    # Count vowels
    vowel_count = count_vowels(text)
    
    # Get detailed information
    details = get_vowel_details(text)
    
    # Display results
    print(f"\n{YELLOW}{'-'*50}{RESET}")
    print(f"{YELLOW}RESULTS".center(50))
    print(f"{YELLOW}{'-'*50}{RESET}")
    print(f"Original text: {CYAN}\"{text}\"{RESET}")
    print(f"Text length: {GREEN}{len(text)}{RESET} characters")
    print(f"Number of vowels: {GREEN}{vowel_count}{RESET}")
    
    if vowel_count > 0:
        print(f"\n{YELLOW}Vowel details:{RESET}")
        print(f"  • Positions (0-indexed): {CYAN}{details['vowel_positions']}{RESET}")
        print(f"  • Vowels found: {GREEN}{', '.join(details['vowel_characters'])}{RESET}")
        
        # Calculate vowel percentage
        vowel_percentage = (vowel_count / len(text)) * 100
        print(f"  • Vowel percentage: {YELLOW}{vowel_percentage:.1f}%{RESET}")
    else:
        print(f"\n{RED}No vowels found in the text!{RESET}")
    
    print(f"{YELLOW}{'-'*50}{RESET}")

if __name__ == "__main__":
    main()