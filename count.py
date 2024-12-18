def count_digits(num):
    count = 0
    while num != 0:
        num //= 10
        count += 1
    return count

# Input from user
number = abs(int(input("Enter a number to count its digits: ")))
print(f"The number of digits in {number} is {count_digits(number)}.")
