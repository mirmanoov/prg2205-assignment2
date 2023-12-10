# Importing necessary modules and functions
from .question_generator import generate_question
from .scoring import update_score, display_score
from data.user_data import save_user_data

def start_game(question_generator, scoring_function, user_data, starting_level):
    print("\nStarting a new game... Good luck!\n")
    play_level(starting_level, question_generator, scoring_function, user_data)  # Use starting_level
    end_game(user_data)

def play_level(level, question_generator, scoring_function, user_data, last_question=None):
    print(f"\nLevel {level}...")

    question_type = question_generator(level)
    question, answer = generate_question(question_type, level, last_question)
    user_answer = input(f"Question: {question} = ")
    user_data['level'] = level

    if user_answer.lower() == 'exit':
        print("Saving your progress and exiting the game...")
        save_user_data(user_data)  # Save progress
        exit() 

    correct = user_answer == str(answer)
    scoring_function(user_data, correct)

    display_score(user_data)

    # Check if the score is below 0, end the game if it is
    if user_data['score'] < 0:
        print("\nYour score has fallen below zero. Game Over.")
        return

    if correct:
        user_data['level'] += 1  
        play_level(level + 1, question_generator, scoring_function, user_data, question)
    else:
        play_level(level, question_generator, scoring_function, user_data, question)


def end_game(user_data):
    print("\nGame Over. Your final score is:")
    display_score(user_data)
    save_user_data(user_data)
    print("Your progress has been saved. Thank you for playing!")
