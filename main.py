# Importing necessary modules
from game_logic.game_core import start_game, end_game
from data.user_data import load_user_data, save_user_data
from utils.higher_order_funcs import question_type_selector, apply_bonus
from game_logic.scoring import update_score

def main():
    user_data = load_user_data()

    print("Welcome to the Educational Math Game!")
    
    while True:
        print("\nMain Menu:")
        print("1. Start Game")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            user_level = user_data['level']  # Extract the user's level

            # Get the question-generating function
            question_generator = question_type_selector()

            # Assigning a scoring function to a variable, with a potential bonus
            scoring_function = apply_bonus(update_score, bonus=5) if user_level > 5 else update_score

            # Passing functions as arguments
            start_game(question_generator, scoring_function, user_data)
        elif choice == '2':
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

    save_user_data(user_data)

if __name__ == "__main__":
    main()
