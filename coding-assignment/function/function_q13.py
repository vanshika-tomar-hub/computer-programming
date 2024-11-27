# 13. Question: Write a function to find the common elements in two lists.
#     Input: Two lists 'list1' and 'list2'.
#     Output: A list containing the common elements of the two lists.
#     Explanation: The function compares the elements in both lists and returns those that appear in both.
def common_elements(list1, list2):
    """Returns a list of common elements between two lists."""
    return list(set(list1) & set(list2))
