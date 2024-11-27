# 19. Question: Write a function to flatten a nested list (list of lists).
#     Input: A nested list 'nested_lst'.
#     Output: A flat list containing all elements from the nested list.
#     Explanation: The function iterates through the sublists and appends all elements into one list.
def flatten_list(nested_lst):
    """Flattens a nested list into a single list."""
    flat_lst = []
    for item in nested_lst:
        if isinstance(item, list):
            flat_lst.extend(flatten_list(item))
        else:
            flat_lst.append(item)
    return flat_lst
