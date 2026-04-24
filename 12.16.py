def digit_to_char(d):
    """Converts a digit to a character (0-15)"""
    digits = "0123456789ABCDEF"
    return digits[d]


def to_base(x, n):
    """Auxiliary recursive function"""
    if x == 0:
        return ''
    return to_base(x // n, n) + digit_to_char(x % n)


def ten_to_n(x, n):
    """
    Converts a natural number x from the decimal
    system to the n-ary system (2 ≤ n ≤ 16).
    """
    if n < 2 or n > 16:
        raise ValueError("2 <= n <= 16")
    if x == 0:
        return '0'
    return to_base(x, n)

print(ten_to_n(100, 8))