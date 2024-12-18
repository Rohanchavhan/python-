# Define two tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Display the original tuples
print("Before Swapping:")
print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)

# Swap the tuples using multiple assignment
tuple1, tuple2 = tuple2, tuple1

# Display the tuples after swapping
print("\nAfter Swapping:")
print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)
