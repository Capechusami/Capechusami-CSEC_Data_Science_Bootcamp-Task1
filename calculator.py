"""
CLI Calculator - Level 3 Task
A command-line calculator with basic arithmetic operations
WITH COLORFUL OUTPUT & ANIMATIONS
"""

import time
import math

# ANSI Color Codes
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    MAGENTA = '\033[95m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
    
    # Rainbow colors
    RAINBOW = [RED, YELLOW, GREEN, CYAN, BLUE, MAGENTA]

def rainbow_text(text: str):
    """Print text in rainbow colors"""
    colors = Colors.RAINBOW
    for i, char in enumerate(text):
        print(f"{colors[i % len(colors)]}{char}{Colors.RESET}", end="")
    print()

def animate_calculation():
    """Show animation while calculating"""
    chars = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    for i in range(10):
        print(f"\r{Colors.YELLOW}{chars[i % len(chars)]} Calculating{Colors.RESET}", end="", flush=True)
        time.sleep(0.03)
    print("\r✓ Done!        ")

class Calculator:
    """A simple calculator class with basic arithmetic operations."""
    
    @staticmethod
    def add(a: float, b: float) -> float:
        return a + b
    
    @staticmethod
    def subtract(a: float, b: float) -> float:
        return a - b
    
    @staticmethod
    def multiply(a: float, b: float) -> float:
        return a * b
    
    @staticmethod
    def divide(a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        return a / b
    
    @staticmethod
    def power(a: float, b: float) -> float:
        return a ** b
    
    @staticmethod
    def modulo(a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Cannot perform modulo by zero!")
        return a % b

def display_menu():
    """Display the calculator menu with colors."""
    print(f"\n{Colors.BOLD}{Colors.MAGENTA}{'='*60}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN}{'🧮 CALCULATOR MENU 🧮'.center(60)}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.MAGENTA}{'='*60}{Colors.RESET}")
    
    menu_items = [
        ("1", "➕ Addition (+)", Colors.GREEN),
        ("2", "➖ Subtraction (-)", Colors.RED),
        ("3", "✖️  Multiplication (*)", Colors.BLUE),
        ("4", "➗ Division (/)", Colors.YELLOW),
        ("5", "🔋 Power (^)", Colors.CYAN),
        ("6", "🔘 Modulo (%)", Colors.MAGENTA),
        ("7", "🚪 Exit", Colors.RED)
    ]
    
    for num, text, color in menu_items:
        print(f"{color}{text.ljust(30)}{Colors.RESET}", end="")
        if int(num) <= 3:
            print("  " * 2)
        else:
            print()
    
    print(f"{Colors.BOLD}{Colors.MAGENTA}{'='*60}{Colors.RESET}")

def get_number(prompt: str) -> float:
    """Get a valid number from user input with colorful prompt."""
    while True:
        try:
            print(f"{Colors.CYAN}{prompt}{Colors.RESET}", end="")
            return float(input())
        except ValueError:
            print(f"{Colors.RED}❌ Invalid input! Please enter a valid number.{Colors.RESET}")

def display_result(a: float, b: float, operation: str, result: float, operator_symbol: str):
    """Display calculation result with beautiful formatting"""
    print(f"\n{Colors.BOLD}{Colors.GREEN}{'='*60}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.YELLOW}🎉 RESULT 🎉{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.GREEN}{'='*60}{Colors.RESET}")
    
    # Format numbers for display (remove .0 if integer)
    a_str = str(int(a) if a.is_integer() else a)
    b_str = str(int(b) if b.is_integer() else b)
    result_str = str(int(result) if result.is_integer() else f"{result:.6f}")
    
    # Display equation with colors
    print(f"\n{Colors.CYAN}{Colors.BOLD}{a_str}{Colors.RESET} "
          f"{Colors.YELLOW}{operator_symbol}{Colors.RESET} "
          f"{Colors.CYAN}{Colors.BOLD}{b_str}{Colors.RESET} "
          f"{Colors.GREEN}={Colors.RESET} "
          f"{Colors.MAGENTA}{Colors.BOLD}{result_str}{Colors.RESET}\n")
    
    # Additional info for certain operations
    if operation == "Division" and b != 0:
        print(f"{Colors.BLUE}💡 {a_str} ÷ {b_str} = {result_str}{Colors.RESET}")
    elif operation == "Power":
        print(f"{Colors.BLUE}💡 {a_str} raised to the power of {b_str} = {result_str}{Colors.RESET}")
    elif operation == "Modulo":
        print(f"{Colors.BLUE}💡 Remainder when {a_str} is divided by {b_str} = {result_str}{Colors.RESET}")
    
    print(f"\n{Colors.BOLD}{Colors.GREEN}{'='*60}{Colors.RESET}")

def perform_calculation(choice: int, calc: Calculator) -> bool:
    """Perform the selected calculation with animations."""
    if choice == 7:
        rainbow_text("\n👋 Thank you for using the calculator! Goodbye!")
        return False
    
    if choice < 1 or choice > 7:
        print(f"\n{Colors.RED}❌ Invalid choice! Please select an option from 1-7.{Colors.RESET}")
        return True
    
    # Get numbers
    print(f"\n{Colors.YELLOW}{'─'*60}{Colors.RESET}")
    a = get_number(f"{Colors.GREEN}🔢 Enter first number: {Colors.RESET}")
    b = get_number(f"{Colors.GREEN}🔢 Enter second number: {Colors.RESET}")
    
    # Animate calculation
    animate_calculation()
    
    try:
        if choice == 1:
            result = calc.add(a, b)
            operation = "Addition"
            operator = "+"
            color = Colors.GREEN
        elif choice == 2:
            result = calc.subtract(a, b)
            operation = "Subtraction"
            operator = "-"
            color = Colors.RED
        elif choice == 3:
            result = calc.multiply(a, b)
            operation = "Multiplication"
            operator = "×"
            color = Colors.BLUE
        elif choice == 4:
            result = calc.divide(a, b)
            operation = "Division"
            operator = "÷"
            color = Colors.YELLOW
        elif choice == 5:
            result = calc.power(a, b)
            operation = "Power"
            operator = "^"
            color = Colors.CYAN
        elif choice == 6:
            result = calc.modulo(a, b)
            operation = "Modulo"
            operator = "%"
            color = Colors.MAGENTA
        else:
            return True
        
        # Display result
        display_result(a, b, operation, result, operator)
        
        # Fun fact about the operation
        fun_facts = {
            "Addition": "➕ Did you know? Addition is commutative: a + b = b + a!",
            "Multiplication": "✖️ Fun fact: Multiplication is repeated addition!",
            "Division": "➗ Division by zero is undefined in mathematics!",
            "Power": "🔋 Powers are also called exponents! 2³ = 2×2×2 = 8",
        }
        
        if operation in fun_facts:
            print(f"{Colors.MAGENTA}{fun_facts[operation]}{Colors.RESET}")
        
    except ValueError as e:
        print(f"\n{Colors.RED}❌ Error: {e}{Colors.RESET}")
    
    return True

def main():
    """Main function to run the calculator."""
    print(f"\n{Colors.BOLD}{Colors.RAINBOW[0]}{'='*60}{Colors.RESET}")
    rainbow_text("        WELCOME TO THE COLORFUL CLI CALCULATOR        ")
    print(f"{Colors.BOLD}{Colors.RAINBOW[0]}{'='*60}{Colors.RESET}")
    
    print(f"\n{Colors.CYAN}✨ Features:{Colors.RESET}")
    print(f"  • {Colors.GREEN}Basic arithmetic operations{Colors.RESET}")
    print(f"  • {Colors.YELLOW}Power and modulo operations{Colors.RESET}")
    print(f"  • {Colors.MAGENTA}Beautiful colorful interface{Colors.RESET}")
    print(f"  • {Colors.BLUE}Error handling{Colors.RESET}\n")
    
    calc = Calculator()
    running = True
    
    while running:
        display_menu()
        try:
            choice = int(input(f"\n{Colors.YELLOW}👉 Enter your choice (1-7): {Colors.RESET}"))
            running = perform_calculation(choice, calc)
            
            if running and choice != 7:
                input(f"\n{Colors.CYAN}Press Enter to continue...{Colors.RESET}")
        except ValueError:
            print(f"{Colors.RED}❌ Invalid input! Please enter a number between 1 and 7.{Colors.RESET}")
            time.sleep(1)

if __name__ == "__main__":
    main()