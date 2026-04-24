def odd_list(a, n):
    """
    A recursive function that, given the first n elements
    of a list a, returns a new list containing only even numbers.
    """
    if n == 0:
        return []
    if a[n-1] % 2 == 0:
        return odd_list(a, n-1) + [a[n-1]]
    return odd_list(a, n-1)

print(odd_list([1, 2, 3, 4, 5, 6, 7, 8], 8))