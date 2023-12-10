def question_type_selector():
    """Returns a lambda function that generates question types based on the user's level."""
    return lambda level: "basic_arithmetic" if level < 5 else \
                         "intermediate_arithmetic" if level < 10 else \
                         "advanced_arithmetic"


def apply_bonus(func, bonus):
    """Returns a new function that applies a bonus to the original function's output."""
    def wrapper(*args, **kwargs):
        original_score = func(*args, **kwargs)
        return original_score + bonus
    return wrapper
