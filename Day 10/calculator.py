
def calcualtion(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operator"
    
def main():
    print("Welcome to the calculator!")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    op = input("Enter the operator (+, -, *, /): ")
    result = calcualtion(num1, num2, op)
    print(f"The result is: {result}")

if __name__ == "__main__":
    main()