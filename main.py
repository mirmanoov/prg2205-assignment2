# Importing necessary modules
from game_logic.game_core import start_game, end_game
from data.user_data import load_user_data, save_user_data
from utils.higher_order_funcs import question_type_selector, apply_bonus
from game_logic.scoring import update_score


import json

def get_scoring_function(user_level):
    return apply_bonus(update_score, bonus=5) if user_level > 5 else update_score

def start_game_with_settings(user_data):
    user_level = user_data['level']
    question_generator = question_type_selector()
    scoring_function = get_scoring_function(user_level)
    start_game(question_generator, scoring_function, user_data, user_level)  

def get_user_data(username):
    try:
        with open('user_data.json', 'r') as f:
            data = json.load(f)
            return data.get(username)  # Retrieve the user data by username key
    except FileNotFoundError:
        return None

def initialize_user_data(username):
    return {'username': username, 'level': 1, 'score': 0}

def main_menu_loop(user_data):
    while True:
        print("\nMain Menu:")
        print("1. Start Game")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            start_game_with_settings(user_data)
            break
        elif choice == '2':
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    print("Welcome to the Educational Math Game!")
    username = input("Please enter your username: ")
    user_data = get_user_data(username)

    if user_data:
        print(f"Welcome back, {username}! Your current level is {user_data['level']}, and your score is {user_data['score']}.")
        if input("Would you like to continue your last game? (yes/no): ").lower() != 'yes':
            user_data = initialize_user_data(username)
            print("Starting a new game session.")
        start_game_with_settings(user_data) 
    else:
        print("No existing game found. Starting a new game for you.")
        user_data = initialize_user_data(username)
        main_menu_loop(user_data)

    save_user_data(user_data)

if __name__ == "__main__":
    main()
