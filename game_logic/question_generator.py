import random
from data.questions_data import questions, filter_questions_by_operation
from utils.math_operations import add, subtract, multiply, apply_operation_to_pairs 

# Separated data handling functions
# 7. Filtering
def get_filtered_questions(operation, symbol, previous_question=None):
    filtered_questions = filter_questions_by_operation(operation, symbol)
    if previous_question:
        # 7. Filtering with 9. Lambdas
        filtered_questions = list(filter(lambda q: q['question'] != previous_question, filtered_questions))
    return filtered_questions

def generate_division_question(max_range):
    """Generate a division question with a whole number as the answer."""
    num2 = random.randint(1, max_range)  # Divisor
    factor = random.randint(1, 10)  # Factor to ensure whole number division
    num1 = num2 * factor  # Dividend
    return f"{num1} / {num2}", num1 // num2

# 3. Create a list of functions and use that list
def generate_basic_arithmetic_question(level, previous_question=None):
    filtered_questions = get_filtered_questions('basic_arithmetic', '+', previous_question) + \
                         get_filtered_questions('basic_arithmetic', '-', previous_question)
    random.shuffle(filtered_questions)
    selected_question = random.choice(filtered_questions)
    return selected_question['question'], selected_question['answer']

def arithmetic_operation(num1, num2, operation):
    # 8. Reducing (conceptual: reducing the operation to a single result)
    return {
        '+': add(num1, num2),
        '-': subtract(num1, num2),
        '*': multiply(num1, num2),
        '/': num1 // num2  # Division operation remains unchanged
    }.get(operation, None)

def generate_intermediate_arithmetic_question(level, last_question=None):
    if random.choice([True, False]):  # 50% chance to generate a pair operations question
        operation = random.choice([add, subtract, multiply])
        # 4. Passing functions as arguments
        return generate_pair_operations_question(operation, num_pairs=2, max_value=50)

    operations = ['+', '-', '*', '/']
    operation = random.choice(operations)
    num1, num2 = random.randint(1, 100), random.randint(1, 100)
    
    if operation == '/':
        return generate_division_question(100)

    answer = arithmetic_operation(num1, num2, operation)
    question = f"{num1} {operation} {num2}"
    
    return question, answer

def advanced_arithmetic_operation(num1, num2, operation):
    if operation == '**':
        # Limit exponentiation range for practicality
        num2 = random.randint(1, 5)
    return arithmetic_operation(num1, num2, operation)

def generate_advanced_arithmetic_question(level, last_question=None):
    if random.choice([True, False]):  # 50% chance to generate a pair operations question
        operation = random.choice([add, subtract, multiply])
        # 4. Passing functions as arguments
        return generate_pair_operations_question(operation, num_pairs=3, max_value=100)

    operations = ['+', '-', '*', '/', '**']
    operation = random.choice(operations)
    num1, num2 = random.randint(1, 1000), random.randint(1, 1000)

    if operation == '/':
        return generate_division_question(1000)

    answer = advanced_arithmetic_operation(num1, num2, operation)
    question = f"{num1} {operation} {num2}"
    
    return question, answer


def generate_pair_operations_question(operation, num_pairs=3, max_value=100):
    """Generate a question that applies an operation to multiple pairs of numbers and sums the results."""
    # 10. List Comprehensions
    pairs = [(random.randint(1, max_value), random.randint(1, max_value)) for _ in range(num_pairs)]
    # 6. Mapping
    results = apply_operation_to_pairs(operation, pairs)
    operation_symbol = {'add': '+', 'subtract': '-', 'multiply': 'x'}.get(operation.__name__, '?')
    question = ' + '.join(f"({pair[0]} {operation_symbol} {pair[1]})" for pair in pairs)
    answer = sum(results)  # 8. Reducing
    return question, answer


# 3. Create a list of functions and use that list
question_generators = [generate_basic_arithmetic_question, generate_intermediate_arithmetic_question, generate_advanced_arithmetic_question, generate_pair_operations_question]

def generate_question(question_type, level, last_question=None):
    generator_index = min(level // 5, len(question_generators) - 1)
    selected_generator = question_generators[generator_index]
    # 4. Passing functions as arguments
    return selected_generator(level, last_question)
