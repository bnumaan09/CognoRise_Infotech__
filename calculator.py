
def calculator():
    print("Simple Calculator App")
    
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    operation = input("Enter operation (+,-,*,/): ")
    
    if operation == '+':
        print(f"The result of addition: {num1 + num2}")
    elif operation == '-':
        print(f"The result of subtraction: {num1 - num2}")
    elif operation == '*':
        print(f"The result of multiplication: {num1 * num2}")
    elif operation == '/':
        if num2 != 0:
            print(f"The result of division: {num1 / num2}")
        else:
            print("Error: Division by zero is not allowed!")
    else:
        print("Invalid operation. Please select from +, -, *, or /.")


calculator()

