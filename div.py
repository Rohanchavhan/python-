def div(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero is not allowed."

# Call the function with two numbers
result = div(10, 2)
print("Division result:", result)
