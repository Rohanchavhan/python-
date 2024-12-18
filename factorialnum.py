def factorial(num):
    if num < 0:
        return "Factorial is not defined for negative numbers."
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

# Input from user
number = int(input("Enter a number to find its factorial: "))
print(f"The factorial of {number} is {factorial(number)}.")
