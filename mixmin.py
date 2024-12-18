import random

# Generate 5 random numbers
numbers = [random.randint(1, 100) for _ in range(5)]

# Display the numbers, maximum, and minimum
print("Random numbers:", numbers)
print("Maximum number:", max(numbers))
print("Minimum number:", min(numbers))
