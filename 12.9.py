def combin(n, k):
    """
    Recursive function for calculating
    the number of combinations C(n, k).
    """
    if k < 0 or k > n or n < 0:
        return 0
    if k == 0 or k == n:
        return 1
    return combin(n - 1, k - 1) + combin(n - 1, k)

print(combin(5, 2))