# Importing necessary modules
from game_logic.game_core import start_game, end_game
from data.user_data import load_user_data, save_user_data
from utils.higher_order_funcs import question_type_selector, apply_bonus
from game_logic.scoring import update_score


import json
# 5. Returning functions
def get_scoring_function(user_level):
    # 9. Lambdas and 4. Passing functions as arguments
    return apply_bonus(update_score, bonus=5) if user_level > 5 else update_score

def start_game_with_settings(user_data):
    user_level = user_data['level']
    # 4. Passing functions as arguments
    question_generator = question_type_selector()
    scoring_function = get_scoring_function(user_level)
    start_game(question_generator, scoring_function, user_data, user_level)  

def get_user_data(username):
    try:
        with open('user_data.json', 'r') as f:
            data = json.load(f)
            # 10. List Comprehensions (indirect, through json.load)
            return data.get(username)  # Retrieve the user data by username key
    except FileNotFoundError:
        return None

def initialize_user_data(username):
    # 1. Separating functions and data
    return {'username': username, 'level': 1, 'score': 0}

def main_menu_loop(user_data):
    options = {
        # press 1 to start game
        '1': start_game_with_settings,
        # press 2 to exit, return false to break loop
        '2': lambda _: print("Exiting the game. Goodbye!") and False,
        # if not 1 or 2, show error message, return true
        'default': lambda _: print("Invalid choice. Please try again.") and True
    }

    print("\nMain Menu:")
    print("1. Start Game")
    print("2. Exit")
    choice = input("Enter your choice: ")

    # if invalid input, print error message, then continue loop
    if options.get(choice, options['default'])(user_data):
        main_menu_loop(user_data)

def main():
    print("Welcome to the Educational Math Game!")
    username = input("Please enter your username: ")
    user_data = get_user_data(username)

    if user_data:
        print(f"Welcome back, {username}! Your current level is {user_data['level']}, and your score is {user_data['score']}.")
        if input("Would you like to continue your last game? (yes/no): ").lower() != 'yes':
            user_data = initialize_user_data(username)
            print("Starting a new game session.")
        # 4. Passing functions as arguments
        start_game_with_settings(user_data) 
    else:
        print("No existing game found. Starting a new game for you.")
        user_data = initialize_user_data(username)
        # 2. Assigning a function to a variable
        main_menu_loop(user_data)

    save_user_data(user_data)

if __name__ == "__main__":
    main()
