# Importing necessary modules and functions
from .question_generator import generate_question
from .scoring import update_score, display_score
from data.user_data import save_user_data

def start_game(question_generator, scoring_function, user_data):
    print("\nStarting a new game... Good luck!\n")
    play_level(1, question_generator, scoring_function, user_data)  # Start at level 1
    end_game(user_data)

def play_level(level, question_generator, scoring_function, user_data):
    print(f"\nLevel {level}...")

    # Game logic for the current level
    question_type = question_generator(level)  # Generate questions based on level
    question, answer = generate_question(question_type)
    user_answer = input(f"Question: {question} = ")

    if user_answer.lower() == 'exit':
        print("Exiting the game...")
        return

    correct = user_answer == str(answer)
    scoring_function(user_data, correct)

    if correct:
        print("Correct! Moving to the next level.")
        play_level(level + 1, question_generator, scoring_function, user_data)  # Recursively call the next level
    else:
        print(f"Incorrect. The right answer was {answer}. Try again.")
        play_level(level, question_generator, scoring_function, user_data)  # Retry the same level

def end_game(user_data):
    print("\nGame Over. Your final score is:")
    display_score(user_data)
    save_user_data(user_data)
    print("Your progress has been saved. Thank you for playing!")
