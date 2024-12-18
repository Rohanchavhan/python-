def search_element(lst, element):
    if element in lst:
        print(f"Element {element} found in the list.")
    else:
        print(f"Element {element} not found in the list.")

# Example list and element to search
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
element_to_search = 4
search_element(numbers, element_to_search)
