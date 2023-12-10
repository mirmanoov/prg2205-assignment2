# Importing necessary modules
from game_logic.game_core import start_game, end_game
from data.user_data import load_user_data, save_user_data
from utils.higher_order_funcs import question_type_selector

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
            question_type = question_type_selector(user_level)()  # Pass the level to the function and call the returned lambda
            start_game(question_type, user_data)
        elif choice == '2':
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

    save_user_data(user_data)

if __name__ == "__main__":
    main()
