def greet_based_on_time(hour):
    # Check if hour is between 5 and 12 (inclusive)
    if 5 <= hour < 12:
        print("Good morning")
    else:
        print("It's not morning")

# Input from user
try:
    hour = int(input("Enter the hour in 24-hour format (0-23): "))
    if 0 <= hour <= 23:
        greet_based_on_time(hour)
    else:
        print("Please enter a valid hour between 0 and 23.")
except ValueError:
    print("Please enter a valid integer for the hour.")
