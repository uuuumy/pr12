def sum_progress(a1, r, n):
    """
    A recursive function for finding the sum of
    the first n terms of an arithmetic progression.
    """
    if n == 1:
        return a1
    return sum_progress(a1, r, n - 1) + (a1 + (n - 1) * r)

print(sum_progress(2, 3, 5))