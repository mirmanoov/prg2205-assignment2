import random

def generate_basic_arithmetic_question():
    operations = ['+', '-', '*', '/']
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operation = random.choice(operations)

    question = f"{num1} {operation} {num2}"
    answer = eval(question)
    return question, answer

def generate_intermediate_arithmetic_question():
    # Implement logic for intermediate arithmetic questions
    # This can be more complex or involve larger numbers
    operations = ['+', '-', '*', '/']
    num1 = random.randint(1, 1000)  # larger range
    num2 = random.randint(1, 1000)
    operation = random.choice(operations)

    question = f"{num1} {operation} {num2}"
    answer = eval(question)
    return question, answer

def generate_advanced_arithmetic_question():
    # Implement logic for advanced arithmetic questions
    # This can include more complex operations or concepts
    operations = ['+', '-', '*', '/', '**']  # Added exponentiation for complexity
    num1 = random.randint(1, 10000)  # even larger range
    num2 = random.randint(1, 10000)
    operation = random.choice(operations)

    # Handling division by zero and integer division
    if operation == '/':
        num1 = num1 * num2  # ensuring a clean division
    elif operation == '**':
        num2 = random.randint(1, 5)  # limiting the power to avoid extremely large numbers

    question = f"{num1} {operation} {num2}"
    answer = eval(question)
    return question, answer

def generate_question(question_type):
    if question_type == 'basic_arithmetic':
        return generate_basic_arithmetic_question()
    # More question types can be added here with elif statements
    else:
        raise ValueError("Unknown question type")

