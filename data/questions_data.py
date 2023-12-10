questions = {
    'basic_arithmetic': [
       {"question": "5 + 7", "answer": 12},
        {"question": "10 - 3", "answer": 7},
        {"question": "4 + 6", "answer": 10},
        {"question": "8 - 2", "answer": 6},
        {"question": "2 + 9", "answer": 11},
        {"question": "7 - 4", "answer": 3},
        {"question": "6 + 5", "answer": 11},
        {"question": "9 - 3", "answer": 6},
        {"question": "1 + 8", "answer": 9},
        {"question": "15 - 7", "answer": 8},
        {"question": "3 + 2", "answer": 5},
        {"question": "4 - 1", "answer": 3},
        {"question": "11 + 6", "answer": 17},
        {"question": "10 - 5", "answer": 5},
        {"question": "14 + 2", "answer": 16},
        {"question": "20 - 8", "answer": 12},
    ],
    'intermediate_arithmetic': [
        {"question": "15 + 23", "answer": 38},
        {"question": "30 - 12", "answer": 18},
        {"question": "7 * 8", "answer": 56},
        {"question": "36 / 6", "answer": 6},
    ],

}

def filter_questions_by_operation(question_type, operation):
    """
    Filter questions based on the arithmetic operation.

    Args:
    question_type (str): The type of questions (e.g., 'basic_arithmetic').
    operation (str): The arithmetic operation to filter by (e.g., '+', '-', '*', '/').

    Returns:
    list: A list of filtered questions.
    """
    if question_type not in questions:
        raise ValueError("Unknown question type")

    return [q for q in questions[question_type] if operation in q["question"]]
