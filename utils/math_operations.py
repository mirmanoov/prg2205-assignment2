def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

def apply_operation_to_pairs(operation, pairs):
    """
    Apply a given operation to a list of number pairs.

    Args:
    operation (function): A function that takes two arguments and performs a calculation.
    pairs (list of tuples): A list of tuples, each containing two numbers.

    Returns:
    list: A list containing the results of applying the operation to each pair.
    """
    return list(map(lambda pair: operation(pair[0], pair[1]), pairs))
