# 15. Question: Write a function to merge two sorted lists into one sorted list.
#     Input: Two sorted lists 'list1' and 'list2'.
#     Output: A single sorted list containing all elements from both lists.
#     Explanation: The function merges the two lists while maintaining their sorted order.
def merge_sorted_lists(list1, list2):
    """Merges two sorted lists into one sorted list."""
    return sorted(list1 + list2)
