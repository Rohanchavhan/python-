def find_last_position(s, substring):
    return s.rfind(substring)

# Input from user
string = input("Enter the main string: ")
substring = input("Enter the substring: ")

position = find_last_position(string, substring)
if position != -1:
    print(f"Last position of '{substring}': {position}")
else:
    print(f"'{substring}' not found in the given string.")
