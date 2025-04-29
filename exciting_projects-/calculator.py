try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    print("What operation do you want to perform?")
    print("Press + for addition")
    print("Press - for subtraction")
    print("Press / for division")
    print("Press * for multiplication")

    op = input("Enter operation: ")

    match op:
        case "+":
            print(f"The result is: {a + b}")
        case "-":
            print(f"The result is: {a - b}")
        case "*":
            print(f"The result is: {a * b}")
        case "/":
            if b != 0:
                print(f"The result is: {a / b}")
            else:
                print("Error: Division by zero is not allowed.")
        case _:
            print("Invalid operation entered.")

except Exception as e:
    print("Error: Please enter valid numbers for a and b.")
