import random

def generate_basic_arithmetic_question():
    operations = ['+', '-', '*', '/']
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operation = random.choice(operations)

    question = f"{num1} {operation} {num2}"
    answer = eval(question)
    return question, answer

def generate_question(question_type):
    if question_type == 'basic_arithmetic':
        return generate_basic_arithmetic_question()
    # More question types can be added here with elif statements
    else:
        raise ValueError("Unknown question type")

