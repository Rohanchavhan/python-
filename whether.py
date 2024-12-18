def can_vote(age):
    return "Eligible to vote." if age >= 18 else "Not eligible to vote."

# Input from user
age = int(input("Enter your age: "))
print(can_vote(age))
