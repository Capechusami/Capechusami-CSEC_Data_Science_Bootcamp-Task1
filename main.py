"""
Main launcher for Day 1 Bootcamp Tasks
Provides a menu to run any of the three tasks
"""

import subprocess
import sys

# Simple color codes
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
MAGENTA = '\033[95m'
RESET = '\033[0m'

def display_main_menu():
    """Display the main menu for selecting tasks."""
    print(f"\n{MAGENTA}{'='*60}{RESET}")
    print(f"{MAGENTA}DAY 1 DATA SCIENCE BOOTCAMP - TASKS".center(60))
    print(f"{MAGENTA}{'='*60}{RESET}")
    print(f"\n{GREEN}Select a task to run:{RESET}")
    print(f"{CYAN}1. Prime Number Checker (Level 1){RESET}")
    print(f"{YELLOW}2. Vowel Counter (Level 2){RESET}")
    print(f"{MAGENTA}3. CLI Calculator (Level 3){RESET}")
    print(f"{RED}4. Exit{RESET}")
    print(f"{MAGENTA}{'-'*60}{RESET}")

def run_script(script_name: str):
    """
    Run a Python script.
    
    Args:
        script_name (str): Name of the script to run
    """
    try:
        print(f"\n{GREEN}Running {script_name}...{RESET}\n")
        subprocess.run([sys.executable, script_name])
    except FileNotFoundError:
        print(f"{RED}Error: {script_name} not found!{RESET}")
    except Exception as e:
        print(f"{RED}Error running {script_name}: {e}{RESET}")

def main():
    """Main function to run the task selector."""
    while True:
        display_main_menu()
        
        try:
            choice = input(f"\n{YELLOW}Enter your choice (1-4): {RESET}").strip()
            
            if choice == '1':
                run_script('prime_checker.py')
            elif choice == '2':
                run_script('vowel_counter.py')
            elif choice == '3':
                run_script('calculator.py')
            elif choice == '4':
                print(f"\n{GREEN}Exiting program. Goodbye!{RESET}")
                break
            else:
                print(f"\n{RED}Invalid choice! Please select 1, 2, 3, or 4.{RESET}")
                
            input(f"\n{CYAN}Press Enter to continue...{RESET}")
            
        except KeyboardInterrupt:
            print(f"\n\n{YELLOW}Program interrupted. Goodbye!{RESET}")
            break
        except Exception as e:
            print(f"\n{RED}An error occurred: {e}{RESET}")

if __name__ == "__main__":
    main()