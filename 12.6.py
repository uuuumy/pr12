def degree5(n):
    """
    A recursive function that determines what
    power a number 5 is raised to, to get n.
    """
    if n == 1:
        return 0
    if n <= 0 or n % 5 != 0:
        return -1
    res = degree5(n // 5)
    return res + 1 if res != -1 else -1

print(degree5(625))