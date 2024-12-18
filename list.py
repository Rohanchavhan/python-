def find_item_in_list(item_list, item_to_find):
    for item in item_list:
        if item == item_to_find:
            return "Item found in the list."
    return "Item not found in the list."

# Input from user
item_list = input("Enter items in the list separated by spaces: ").split()
item_to_find = input("Enter the item to search for: ")
print(find_item_in_list(item_list, item_to_find))
