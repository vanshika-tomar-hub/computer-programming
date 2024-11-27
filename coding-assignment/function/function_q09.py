# 9. Question: Write a function to check if a string is a palindrome.
#    Input: A string 's'.
#    Output: True if the string is a palindrome, False otherwise.
#    Explanation: A palindrome is a word, phrase, or sequence that reads the same backward as forward.
def is_palindrome(s):
    """Returns True if the string is a palindrome, otherwise False."""
    s = s.lower().replace(" ", "")
    return s == s[::-1]
