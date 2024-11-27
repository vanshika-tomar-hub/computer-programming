# 2. Question: Write a function to calculate the factorial of a number.
#    Input: A single integer 'n'.
#    Output: The factorial of 'n' (n!).
#    Explanation: The factorial of a number is the product of all positive integers less than or equal to the number.
def factorial(n):
    """Returns the factorial of a number."""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
