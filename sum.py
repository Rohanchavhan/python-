def sum_first_10_natural_numbers():
    total = 0
    for i in range(1, 11):
        total += i
    return total

print(f"The sum of the first 10 natural numbers is {sum_first_10_natural_numbers()}.")
