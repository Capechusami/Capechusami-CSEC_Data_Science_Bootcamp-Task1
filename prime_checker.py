"""
Prime Number Checker - Level 1 Task
Checks whether a given number is prime or not
"""

# Simple color codes
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
RESET = '\033[0m'

def is_prime(n: int) -> bool:
    """
    Check if a number is prime.
    
    A prime number is a natural number greater than 1 that has no positive 
    divisors other than 1 and itself.
    
    Args:
        n (int): The number to check
        
    Returns:
        bool: True if the number is prime, False otherwise
        
    Examples:
        >>> is_prime(7)
        True
        >>> is_prime(10)
        False
        >>> is_prime(1)
        False
    """
    # Handle edge cases
    if n <= 1:
        return False
    
    # 2 is the only even prime number
    if n == 2:
        return True
    
    # Eliminate all other even numbers
    if n % 2 == 0:
        return False
    
    # Check odd divisors from 3 to sqrt(n)
    # We only need to check up to square root because if n = a * b,
    # at least one factor is <= sqrt(n)
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2  # Skip even numbers
    
    return True

def get_user_input() -> int:
    """
    Get and validate user input for a number.
    
    Returns:
        int: Valid integer from user input
    """
    while True:
        try:
            number = int(input(f"{CYAN}Enter a number to check if it's prime: {RESET}"))
            return number
        except ValueError:
            print(f"{RED}Invalid input! Please enter a valid integer.{RESET}")

def main():
    """Main function to run the prime number checker."""
    print(f"{YELLOW}{'='*50}{RESET}")
    print(f"{YELLOW}PRIME NUMBER CHECKER".center(50))
    print(f"{YELLOW}{'='*50}{RESET}")
    print("A prime number is a natural number greater than 1")
    print("that has no positive divisors other than 1 and itself.\n")
    
    # Get user input
    number = get_user_input()
    
    # Check if the number is prime
    result = is_prime(number)
    
    # Display result
    print(f"\n{YELLOW}{'-'*50}{RESET}")
    if result:
        print(f"{GREEN}✓ {number} IS a prime number!".center(50))
        print(f"{GREEN}Congratulations! 🎉{RESET}".center(50))
    else:
        print(f"{RED}✗ {number} is NOT a prime number.{RESET}".center(50))
    print(f"{YELLOW}{'-'*50}{RESET}")
    
    # Provide additional information for non-prime numbers
    if not result and number > 1:
        # Find first divisor for demonstration
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                print(f"\n{YELLOW}Reason: {number} = {i} × {number // i}{RESET}")
                break

if __name__ == "__main__":
    main()