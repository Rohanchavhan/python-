def find_max(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

# Input from user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print(f"The maximum of {num1} and {num2} is {find_max(num1, num2)}.")
