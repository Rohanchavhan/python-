def remove_duplicates_and_sort(lst):
    unique_lst = list(set(lst))  # Remove duplicates using set
    unique_lst.sort()  # Sort the list
    print(f"List after removing duplicates and sorting: {unique_lst}")

# Example list
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
remove_duplicates_and_sort(numbers)
