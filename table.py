def multiplication_table(number):
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

# Input from user
number = int(input("Enter a number to get its multiplication table: "))
multiplication_table(number)
