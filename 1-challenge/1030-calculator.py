while True:
    num1 = float(input("Choose a number: "))
    num2 = float(input("Choose another one: "))
    operation = input("Choose an operation: \n\tOptions are: +, -, * or /.\n\tWrite 'exit' to finish.\n")

    if operation == 'exit':
        print("Calculator exited.")
        break
    elif operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        result = num1 / num2
    else:
        print("Invalid operation.")
        continue

    print("Result:", result)
