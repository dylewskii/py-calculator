import art

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculate():
    print(art.logo)
    num1 = float(input("Enter your first number: "))
    for key in operations:
        print(key)

    should_continue = True
    while should_continue:
        symbol = input("Pick an operation: ")
        num2 = float(input("Enter the next number: "))

        answer = operations[symbol](num1, num2)
        print(f"{num1} {symbol} {num2} = {answer}")
        choice = input(f"Type 'y' to continue calculating with xxx, or type 'n' to exit.")
        if choice == 'y':
            num1 = answer
        else:
            should_continue = False
            calculate()



calculate()

