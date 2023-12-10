# Importing necessary modules
from game_logic.game_core import start_game, end_game
from data.user_data import load_user_data, save_user_data
from utils.higher_order_funcs import question_type_selector, apply_bonus
from game_logic.scoring import update_score
import json

def start_game_directly(user_data):
    user_level = user_data['level']
    question_generator = question_type_selector()
    scoring_function = apply_bonus(update_score, bonus=5) if user_level > 5 else update_score
    start_game(question_generator, scoring_function, user_data, user_level)  


    
def get_user_data(username):
    try:
        with open('user_data.json', 'r') as f:
            data = json.load(f)
            user_data = data.get(username)  # Retrieve the user data by username key
            if user_data:
                return user_data
            return None
    except FileNotFoundError:
        return None


def main():
    print("Welcome to the Educational Math Game!")
    username = input("Please enter your username: ")
    user_data = get_user_data(username)

    if user_data:
        print(f"Welcome back, {username}! Your current level is {user_data['level']}, and your score is {user_data['score']}.")
        choice = input("Would you like to continue your last game? (yes/no): ")
        if choice.lower() == 'no':
            user_data = {'username': username, 'level': 1, 'score': 0}
            print("Starting a new game session.")
        else:
            print("Continuing your last game.")
            user_level = user_data['level']
            question_generator = question_type_selector()
            scoring_function = apply_bonus(update_score, bonus=5) if user_level > 5 else update_score
            start_game(question_generator, scoring_function, user_data, user_level)  # Directly call start_game here
            return  # Exit the main function after the game is over
    else:
        user_data = {'username': username, 'level': 1, 'score': 0}
        print("No existing game found. Starting a new game for you.")
        
    # The main menu loop is now only relevant for new games or if the user chooses not to continue
    while True:
        print("\nMain Menu:")
        print("1. Start Game")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            user_level = user_data['level']
            question_generator = question_type_selector()
            scoring_function = apply_bonus(update_score, bonus=5) if user_level > 5 else update_score
            start_game(question_generator, scoring_function, user_data, user_level)  # Pass user_level here
            break  # Break the loop after the game is over
        elif choice == '2':
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

    save_user_data(user_data)

def start_game_directly(user_data):
    user_level = user_data['level']
    question_generator = question_type_selector()
    scoring_function = apply_bonus(update_score, bonus=5) if user_level > 5 else update_score
    start_game(question_generator, scoring_function, user_data)

if __name__ == "__main__":
    main()

