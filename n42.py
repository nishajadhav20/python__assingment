'''code for calculator operation using match case'''

num1 = int (input("Enter  the number 1 = "))  
num2 = int (input("Enter  the number 2= "))    



print("\n--- Select Operation ---")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("\nEnter your choice (1-4): "))

match choice:
    case 1:
        result = num1 + num2
        print(f"Result: {num1} + {num2} = {result}")
    case 2:
        result = num1 - num2
        print(f"Result: {num1} - {num2} = {result}")
    case 3:
        result = num1 * num2
        print(f"Result: {num1} * {num2} = {result}")
    case 4:

        if num2 != 0:
            result = num1 / num2
            print(f"Result: {num1} / {num2} = {result}")
        else:
            print("Error: Division by zero is not allowed!")
    case _:
        print("Invalid choice! Please select between 1 and 4.")  