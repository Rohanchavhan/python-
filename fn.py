def factorial(num):
    if num < 0:
        return "Factorial is not defined for negative numbers."
    result = 1
    while num > 1:
        result *= num
        num -= 1
    return result

# Input from user
number = int(input("Enter a number to find its factorial: "))
print(f"The factorial of {number} is {factorial(number)}.")
