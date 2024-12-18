def check_voting_eligibility(age):
    if age >= 18:
        return "You are eligible to vote."
    else:
        return "You are not eligible to vote."

# Get the user's age
try:
    age = int(input("Enter your age: "))
    print(check_voting_eligibility(age))
except ValueError:
    print("Please enter a valid number for age.")
