def second_smallest(lst):
    unique_lst = list(set(lst))  # Remove duplicates
    unique_lst.sort()  # Sort the list
    if len(unique_lst) > 1:
        print(f"Second smallest element: {unique_lst[1]}")
    else:
        print("List does not have a second smallest element.")

# Example list
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
second_smallest(numbers)
