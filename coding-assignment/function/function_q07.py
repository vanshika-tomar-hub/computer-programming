# 7. Question: Write a function to count the number of vowels in a string.
#    Input: A string 's'.
#    Output: The count of vowels (a, e, i, o, u) in the string.
#    Explanation: The function iterates through the string and counts the characters that are vowels.
def count_vowels(s):
    """Returns the number of vowels in a string."""
    return sum(1 for char in s.lower() if char in 'aeiou')
