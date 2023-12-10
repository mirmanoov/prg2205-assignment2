def update_score(user_data, is_correct):
    """Update the user's score based on the correctness of their answer."""
    if is_correct:
        user_data['score'] += 10  # Increment score for correct answer
    else:
        user_data['score'] -= 5   # Decrement score for incorrect answer, if applicable

def display_score(user_data):
    """Display the current score of the user."""
    print(f"Current Score: {user_data['score']}")
