def print_patterns(n):
    # Pattern 1: Star triangle
    print("Pattern 1:")
    for i in range(1, n + 1):
        print("* " * i)
    print()

    # Pattern 2: Consecutive numbers triangle
    print("Pattern 2:")
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
    print()

    # Pattern 3: Same row number triangle
    print("Pattern 3:")
    for i in range(1, n + 1):
        print((str(i) + " ") * i)
    print()

# Input from user for number of rows
n = int(input("Enter the number of rows for the triangle patterns: "))
print_patterns(n)

