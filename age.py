from datetime import datetime

def calculate_age(birth_date):
    today = datetime.today()
    age = today.year - birth_date.year

    # Adjust age if the birthday hasn't occurred yet this year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    
    return age

# Input in YYYY-MM-DD format
birth_date_input = input("Enter your date of birth (YYYY-MM-DD): ")

try:
    birth_date = datetime.strptime(birth_date_input, "%Y-%m-%d")
    age = calculate_age(birth_date)
    print(f"You are {age} years old.")
except ValueError:
    print("Invalid date format. Please use YYYY-MM-DD.")
