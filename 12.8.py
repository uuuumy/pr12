def fib(k):
    """
    Recursive function to calculate the k-th term of the Fibonacci sequence.
    """
    if k == 1 or k == 2:
        return 1
    if k <= 0:
        raise ValueError("k >= 1")
    return fib(k - 1) + fib(k - 2)

print(fib(10))      