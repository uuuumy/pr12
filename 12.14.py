def numbers(x):
    """
    A recursive function that prints the digits of a
    natural number x in reverse order, with each digit on a separate line.
    """
    if x < 10:
        print(x)
    else:
        print(x % 10)
        numbers(x // 10)

numbers(234)