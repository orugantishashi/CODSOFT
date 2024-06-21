def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def get_operation_choice():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    choice = input("Enter choice (1/2/3/4): ")
    while choice not in ['1', '2', '3', '4']:
        print("Invalid choice. Please select a valid operation.")
        choice = input("Enter choice (1/2/3/4): ")
    return choice

def get_number(prompt):
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def perform_calculation(choice, num1, num2):
    if choice == '1':
        return add(num1, num2)
    elif choice == '2':
        return subtract(num1, num2)
    elif choice == '3':
        return multiply(num1, num2)
    elif choice == '4':
        return divide(num1, num2)

def calculator():
    num1 = get_number("Enter first number: ")
    num2 = get_number("Enter second number: ")
    choice = get_operation_choice()
    result = perform_calculation(choice, num1, num2)
    print(f"The result is: {result}")

if __name__ == "__main__":
    calculator()
