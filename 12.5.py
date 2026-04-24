def mod_number(a, b):
    """
    Recursive function to find the remainder of a divided by b
    """
    if b == 0:
        raise ValueError("на 0 делить нельзя")
    if a < b:
        return a
    return mod_number(a - b, b)

print(mod_number(20, 4))