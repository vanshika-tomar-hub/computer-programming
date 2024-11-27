# 3. Question: Write a function to check if a number is prime.
#    Input: A single integer 'n'.
#    Output: True if 'n' is a prime number, False otherwise.
#    Explanation: A prime number is a number greater than 1 that has no divisors other than 1 and itself.
def is_prime(n):
    """Returns True if the number is prime, otherwise False."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
