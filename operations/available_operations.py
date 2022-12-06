def custom_sum():
    num_1 = float(input('Write first num: '))
    num_2 = float(input('Write second num: '))
    print(num_1 + num_2)


def custom_diff():
    num_1 = float(input('Write first num: '))
    num_2 = float(input('Write second num: '))
    print(num_1 - num_2)

def custom_multiply():
    num_1 = float(input('Write first num: '))
    num_2 = float(input('Write second num: '))
    print(num_1 * num_2)

def custom_division():
    num_1 = float(input('Write first num: '))
    num_2 = float(input('Write second num: '))
    try:
        print(num_1 / num_2)
    except ZeroDivisionError:
        print("You can't division by zero! Choose another numbers or operation.")


def left_calculator():
    exit("Thanks for using our calculator. See you soon!")


OPERATIONS_MAPPING = {
    'sum': custom_sum,
    'diff': custom_diff,
    'multiply': custom_multiply,
    'division': custom_division,
    'exit': left_calculator
}