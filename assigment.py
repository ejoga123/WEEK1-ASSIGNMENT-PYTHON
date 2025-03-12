def calculator():
    try:
        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")
        
        if not num1.replace('.', '', 1).isdigit() or not num2.replace('.', '', 1).isdigit():
            print("Invalid input. Please enter valid numerical values.")
            return
        
        num1 = float(num1)
        num2 = float(num2)
        operator = input("Enter an operator (+, -, *, /): ").strip()
        
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                return
            result = num1 / num2
        else:
            print("Invalid operator. Please enter one of +, -, *, /")
            return
        
        print(f"{num1} {operator} {num2} = {result}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    calculator()
