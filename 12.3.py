def progress(a1, r, n):
    """
    Recursive function for finding the
    n-th term of an arithmetic progression.
    """
    if n == 1:
        return a1
    return progress(a1, r, n - 1) + r

print(progress(10, 5, 3))