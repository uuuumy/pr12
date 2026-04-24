def pownum(a, n):
    """Recursive function to calculate a^n"""
    if n == 0:
        return 1.0
    return a * pownum(a, n - 1)

print(pownum(7,1))