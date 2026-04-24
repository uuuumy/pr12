def count(a, b):
    """Determines the number of squares"""
    if a == 0 or b == 0:
        return 0
    if a < b:
        a, b = b, a

    num_squares_this_step = a // b
    return num_squares_this_step + count(b, a % b)

print(count(5, 3))