# Importing necessary modules and functions
from .question_generator import generate_question
from .scoring import update_score, display_score
from data.user_data import save_user_data


def start_game(question_generator, scoring_function, user_data, starting_level):
    print("\nStarting a new game... Good luck!\n")
    play_level(starting_level, question_generator, scoring_function, user_data)

def play_level(level, question_generator, scoring_function, user_data):
    print(f"\nLevel {level}...")

    question_type = question_generator(level)
    question, answer = generate_question(question_type, level)
    user_answer = input(f"Question: {question} = ")
    user_data['level'] = level

    handle_exit(user_answer, user_data)

    correct = user_answer == str(answer)
    update_score(user_data, correct)
    display_score(user_data)

    check_score_and_continue(user_data, correct, level, question_generator, scoring_function)

def handle_exit(user_answer, user_data):
    if user_answer.lower() == 'exit':
        print("Saving your progress and exiting the game...")
        save_user_data(user_data)
        exit()

def check_score_and_continue(user_data, correct, level, question_generator, scoring_function):
    if user_data['score'] < 0:
        print("\nYour score has fallen below zero. Game Over.")
        return

    next_level = level + 1 if correct else level
    play_level(next_level, question_generator, scoring_function, user_data)

def end_game(user_data):
    print("\nGame Over. Your final score is:")
    display_score(user_data)
    save_user_data(user_data)
    print("Your progress has been saved. Thank you for playing!")
