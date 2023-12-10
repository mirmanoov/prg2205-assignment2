from functools import reduce

# Separating function and data
def calculate_score(is_correct):
    """Return the score for a single answer."""
    return 10 if is_correct else -5

# Assigning a function to a variable and creating a list of functions
score_updater = calculate_score

# Using mapping and reducing for updating total score
def update_total_score(answers):
    """Update the total score based on a list of answer outcomes."""
    # Using map to apply calculate_score to each answer, then reduce to aggregate the score
    total_score = reduce(lambda acc, is_correct: acc + score_updater(is_correct), map(calculate_score, answers), 0)
    return total_score

# Refactored to use the score_updater function
def update_score(user_data, is_correct):
    """Update the user's score based on the correctness of their answer."""
    user_data['score'] += score_updater(is_correct)

def display_score(user_data):
    """Display the current score of the user."""
    print(f"Current Score: {user_data['score']}")

