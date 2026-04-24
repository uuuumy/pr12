def simmetr(s, i, j):
    """
    Determines whether the portion of string s, starting with the
    i-th character and ending with the j-th character, is symmetric.
    """
    if i >= j:
        return True

    if s[i] != s[j]:
        return False
    return simmetr(s, i + 1, j - 1)

print(simmetr('a', 0, 0))