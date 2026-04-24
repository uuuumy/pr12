def search(a, x):
    """
    A recursive function that determines
    whether a number x is present in a list a.
    """
    if not a:
        return 0
    if a[0] == x:
        return 1
    return search(a[1:], x)

print(search([10, 20, 30, 40], 30))