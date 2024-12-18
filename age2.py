from datetime import date

def calculate_age(birthdate):
    today = date.today()
    age_years = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age_years

def main():
    birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")
    year, month, day = map(int, birthdate_str.split('-'))
    birthdate = date(year, month, day)
    age = calculate_age(birthdate)
    print(f"You are {age} years old.")

if __name__ == "__main__":
    main()