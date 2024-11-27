# 6. Question: Write a function to check if a number is even or odd.
#    Input: A single integer 'n'.
#    Output: "Even" if 'n' is even, "Odd" if 'n' is odd.
#    Explanation: A number is even if it is divisible by 2; otherwise, it is odd.
def even_or_odd(n):
    """Returns 'Even' if the number is even, 'Odd' if the number is odd."""
    return "Even" if n % 2 == 0 else "Odd"
