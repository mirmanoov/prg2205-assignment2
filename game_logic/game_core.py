# Importing necessary modules and functions
from .question_generator import generate_question
from .scoring import update_score, display_score
from data.user_data import save_user_data

def start_game(question_type, user_data):
    print("\nStarting a new game... Good luck!\n")

    game_active = True
    while game_active:
        question, answer = generate_question(question_type)
        user_answer = input(f"Question: {question} = ")

        if user_answer.lower() == 'exit':
            game_active = False
            print("Exiting the game...")
            continue

        correct = user_answer == str(answer)
        update_score(user_data, correct)

        if correct:
            print("Correct!")
        else:
            print(f"Incorrect. The right answer was {answer}.")

        display_score(user_data)

    end_game(user_data)

def end_game(user_data):
    print("\nGame Over. Your final score is:")
    display_score(user_data)
    save_user_data(user_data)
    print("Your progress has been saved. Thank you for playing!")
