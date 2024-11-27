# 12. Question: Write a function to find the length of a string without using the built-in 'len()' function.
#     Input: A string 's'.
#     Output: The length of the string 's'.
#     Explanation: The function iterates through the string and counts the number of characters.

def length_of_string(s):
    """Returns the length of a string."""
    count = 0
    for char in s:
        count += 1
    return count
