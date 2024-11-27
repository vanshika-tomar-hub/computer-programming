# 11. Question: Write a function to convert a decimal number to binary.
#     Input: A single integer 'n'.
#     Output: The binary representation of 'n' as a string.
#     Explanation: The function converts the decimal number into its binary equivalent.
def decimal_to_binary(n):
    """Returns the binary representation of a number."""
    return bin(n)[2:]
