def nod(a, b):
    """
    Recursive function to calculate the greatest common divisor.
    """
    if b == 0:
        return a
    return nod(b, a % b)

print(nod(48, 18))