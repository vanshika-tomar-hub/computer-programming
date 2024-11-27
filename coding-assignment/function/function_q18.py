# 18. Question: Write a function to find the maximum and minimum of a list.
#     Input: A list 'lst'.
#     Output: A tuple (max, min) containing the maximum and minimum values of the list.
#     Explanation: The function returns the highest and lowest values found in the list.
def max_min(lst):
    """Returns the maximum and minimum values in the list."""
    return max(lst), min(lst)
