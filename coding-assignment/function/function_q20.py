# 20. Question: Write a function to sort a list of tuples based on the second element of each tuple.
#     Input: A list of tuples 'lst'.
#     Output: The list sorted by the second element of each tuple.
#     Explanation: The function sorts the list using the second element of each tuple as the sorting key.
def sort_by_second_element(lst):
    """Sorts a list of tuples based on the second element."""
    return sorted(lst, key=lambda x: x[1])
