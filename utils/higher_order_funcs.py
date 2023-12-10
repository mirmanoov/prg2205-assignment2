def question_type_selector(level):
    """Returns a function that generates questions based on the user's level."""
    if level < 5:
        return lambda: "basic_arithmetic"
    elif level < 10:
        return lambda: "intermediate_arithmetic"
    # More levels and types can be added here
    else:
        return lambda: "advanced_arithmetic"

def apply_bonus(func, bonus):
    """Returns a new function that applies a bonus to the original function's output."""
    def wrapper(*args, **kwargs):
        original_score = func(*args, **kwargs)
        return original_score + bonus
    return wrapper
