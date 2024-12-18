def fibonacci_series(n):
    a, b = 0, 1
    count = 0
    while count < n:
        print(a, end=" ")
        a, b = b, a + b
        count += 1

# Input from user
n_terms = int(input("Enter the number of terms for the Fibonacci series: "))
print(f"Fibonacci series up to {n_terms} terms:")
fibonacci_series(n_terms)
