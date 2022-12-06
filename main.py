from operations.available_operations import OPERATIONS_MAPPING

LIST_OF_OPERATIONS = {'sum', 'diff', 'multiply', 'division', 'exit'}


if __name__ == '__main__':
    while True:
        operation = input(f'Please write the operation. One of {LIST_OF_OPERATIONS}: ')
        if operation not in LIST_OF_OPERATIONS:
            print(f"Oops! I don't know this operation. Please enter one of operations from {LIST_OF_OPERATIONS} below.")
            continue
        OPERATIONS_MAPPING[operation]()

