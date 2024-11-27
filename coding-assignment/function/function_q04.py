# 4. Question: Write a function to find the largest of three numbers.
#    Input: Three integers 'a', 'b', 'c'.
#    Output: The largest of the three integers.
#    Explanation: The function will return the maximum number among the three inputs.
def fibonacci(n):
    """Returns the Fibonacci sequence up to 'n' terms."""
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[:n]
