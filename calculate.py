def sum_of_digits(num):
    total = 0
    while num != 0:
        total += num % 10
        num //= 10
    return total

# Input from user
number = abs(int(input("Enter a number to find the sum of its digits: ")))
print(f"The sum of digits of {number} is {sum_of_digits(number)}.")
