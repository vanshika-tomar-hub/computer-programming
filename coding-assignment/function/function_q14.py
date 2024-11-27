# 14. Question: Write a function to remove duplicates from a list.
#     Input: A list 'lst'.
#     Output: A list with duplicate elements removed.
#     Explanation: The function removes all repeated elements, leaving only unique values.
def remove_duplicates(lst):
    """Returns a list with duplicate elements removed."""
    return list(set(lst))
