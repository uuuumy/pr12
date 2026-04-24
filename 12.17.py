def is_prime_recursive_helper(n, current_divisor):
    """Simplicity check"""
    if n % current_divisor == 0:
        return 0
    if current_divisor * current_divisor > n:
        return 1
    return is_prime_recursive_helper(n, current_divisor + 1)

def function1(x):
    """Determines whether a natural number x is prime"""
    if x <= 1:
        return 0
    if x == 2:
        return 1
    if x % 2 == 0:
        return 0
    return is_prime_recursive_helper(x, 3)

print(function1(11))