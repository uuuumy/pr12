def count(n):
    """
    Recursive function for counting the
    number of digits in a natural number n.
    """
    if n < 10:
        return 1
    return 1 + count(n // 10)

print(count(7222))