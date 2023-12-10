# Importing necessary modules and functions
from .question_generator import generate_question
from .scoring import update_score, display_score
from data.user_data import save_user_data

# 4. Passing functions as arguments
def start_game(question_generator, scoring_function, user_data, starting_level):
    print("\nStarting a new game... Good luck!\n")
    # 4. Passing functions as arguments
    play_level(starting_level, question_generator, scoring_function, user_data)

# 4. Passing functions as arguments
def play_level(level, question_generator, scoring_function, user_data):
    print(f"\nLevel {level}...")

    # 4. Passing functions as arguments
    question_type = question_generator(level)
    question, answer = generate_question(question_type, level)
    user_answer = input(f"Question: {question} = ")
    user_data['level'] = level
    
    # 4. Passing functions as arguments
    handle_exit(user_answer, user_data)

    correct = user_answer == str(answer)
    # 4. Passing functions as arguments
    update_score(user_data, correct)
    display_score(user_data)
    
    # 11. Recursion
    check_score_and_continue(user_data, correct, level, question_generator, scoring_function)

def handle_exit(user_answer, user_data):
    if user_answer.lower() == 'exit':
        print("Saving your progress and exiting the game...")
        save_user_data(user_data)
        exit()

# 4. Passing functions as arguments and 11. Recursion
def check_score_and_continue(user_data, correct, level, question_generator, scoring_function):
    if user_data['score'] < 0:
        print("\nYour score has fallen below zero. Game Over.")
        return

    next_level = level + 1 if correct else level
    # 11. Recursion
    play_level(next_level, question_generator, scoring_function, user_data)

def end_game(user_data):
    print("\nGame Over. Your final score is:")
    display_score(user_data)
    save_user_data(user_data)
    print("Your progress has been saved. Thank you for playing!")
