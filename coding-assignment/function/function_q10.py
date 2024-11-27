# 10. Question: Write a function to calculate the sum of digits of a number.
#     Input: A single integer 'n'.
#     Output: The sum of the digits of 'n'.
#     Explanation: The function will break down the number into its digits and return their sum.
def sum_of_digits(n):
    """Returns the sum of the digits of the number."""
    return sum(int(digit) for digit in str(n))
