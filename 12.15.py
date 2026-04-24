def to_bin(n):
    """Auxiliary recursive function"""
    if n == 0:
        return ''
    return to_bin(n // 2) + str(n % 2)


def ten_to_bin(x):
    """
    Recursive function for converting a
    natural number x from decimal to binary.
    """
    if x == 0:
        return '0'
    return to_bin(x)

print(ten_to_bin(10))
