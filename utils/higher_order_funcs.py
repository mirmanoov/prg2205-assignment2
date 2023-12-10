# 5. Returning functions and 9. Lambdas
def question_type_selector():
    """Returns a lambda function that generates question types based on the user's level."""
    # 9. Lambdas: Returning a lambda function that takes a level and returns a question type
    return lambda level: "basic_arithmetic" if level < 5 else \
                         "intermediate_arithmetic" if level < 10 else \
                         "advanced_arithmetic"

# 5. Returning functions
def apply_bonus(func, bonus):
    """Returns a new function that applies a bonus to the original function's output.

    This is an example of a higher-order function that takes a function as an argument 
    and returns another function."""
     # 4. Passing functions as arguments: 'func' is passed as an argument
    def wrapper(*args, **kwargs):
        # Invoking the passed function with arguments
        original_score = func(*args, **kwargs)
        # Modifying the function's output
        return original_score + bonus
    # Returning a new function
    return wrapper
