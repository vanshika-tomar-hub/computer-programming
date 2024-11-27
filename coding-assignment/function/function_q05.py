# 5. Question: Write a function to return the Fibonacci sequence up to 'n' terms.
#    Input: A single integer 'n'.
#    Output: A list containing the Fibonacci sequence up to 'n' terms.
#    Explanation: The Fibonacci sequence starts with 0, 1, and each subsequent number is the sum of the previous two.
def fibonacci(n):
    """Returns the Fibonacci sequence up to 'n' terms."""
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[:n]
