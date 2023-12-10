import random
from data.questions_data import questions, filter_questions_by_operation

def generate_division_question(max_range):
    """Generate a division question with a whole number as the answer."""
    num2 = random.randint(1, max_range)  # Divisor
    factor = random.randint(1, 10)  # Factor to ensure whole number division
    num1 = num2 * factor  # Dividend
    return f"{num1} / {num2}", num1 // num2

def generate_basic_arithmetic_question(level, previous_question=None):
    # Only for levels below 5
    filtered_questions = filter_questions_by_operation('basic_arithmetic', '+') + \
                         filter_questions_by_operation('basic_arithmetic', '-')
    
    # Remove the previous question to avoid repetition
    if previous_question:
        filtered_questions = [q for q in filtered_questions if q['question'] != previous_question]

    random.shuffle(filtered_questions)
    selected_question = random.choice(filtered_questions)
    return selected_question['question'], selected_question['answer']



def generate_intermediate_arithmetic_question(level):
    operations = ['+', '-', '*', '/']
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operation = random.choice(operations)

    if operation == '/':
        question, answer = generate_division_question(100)
    else:
        question = f"{num1} {operation} {num2}"
        answer = eval(question)

    return question, answer

def generate_advanced_arithmetic_question(level):
    operations = ['+', '-', '*', '/', '**']
    num1 = random.randint(1, 1000)
    num2 = random.randint(1, 1000)
    operation = random.choice(operations)

    if operation == '/':
        question, answer = generate_division_question(1000)
    elif operation == '**':
        num2 = random.randint(1, 5)
        question = f"{num1} {operation} {num2}"
        answer = eval(question)
    else:
        question = f"{num1} {operation} {num2}"
        answer = eval(question)

    return question, answer


def generate_question(question_type, level, last_question=None):
    if level < 5:
        return generate_basic_arithmetic_question(level, last_question)
    elif level < 10:
        return generate_intermediate_arithmetic_question(level)  # Assuming no last_question needed for intermediate
    else:
        return generate_advanced_arithmetic_question(level)      # Assuming no last_question needed for advanced

