# Simple Python Calculator

print("Simple Python Calculator")
print("Select Operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

choice = input("Enter choice (1/2/3/4): ")

if choice == '1':
    print("Result:", num1 + num2)

elif choice == '2':
    print("Result:", num1 - num2)

elif choice == '3':
    print("Result:", num1 * num2)

elif choice == '4':
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error! Division by zero.")

else:
    print("Invalid input")