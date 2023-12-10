from functools import reduce

def calculate_score(is_correct):
    """Return the score for a single answer."""
    return 10 if is_correct else -5

def update_total_score(answers):
    """Update the total score based on a list of answer outcomes."""
    # Using reduce to aggregate the score
    total_score = reduce(lambda acc, is_correct: acc + calculate_score(is_correct), answers, 0)
    return total_score

def update_score(user_data, is_correct):
    """Update the user's score based on the correctness of their answer."""
    user_data['score'] += calculate_score(is_correct)

def display_score(user_data):
    """Display the current score of the user."""
    print(f"Current Score: {user_data['score']}")
