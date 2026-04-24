def maxlist(a):
    """
    A recursive function for finding the
    maximum element in a list of integers.
    """
    if not a:
        raise ValueError("список пустой")
    if len(a) == 1:
        return a[0]

    max_rest = maxlist(a[1:])
    return a[0] if a[0] > max_rest else max_rest

print(maxlist([3, 7, 2, -9, 1]))