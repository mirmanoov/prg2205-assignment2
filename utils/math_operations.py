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

# 6. Mapping and 9. Lambdas
def apply_operation_to_pairs(operation, pairs):
    """
    Apply a given operation to a list of number pairs.

    Args:
    operation (function): A function that takes two arguments and performs a calculation.
    pairs (list of tuples): A list of tuples, each containing two numbers.

    Returns:
    list: A list containing the results of applying the operation to each pair.
    """
    # 6. Mapping: Applying the operation to each pair
    # 9. Lambdas: Using a lambda to pass the pair elements to the operation
    return list(map(lambda pair: operation(pair[0], pair[1]), pairs))
