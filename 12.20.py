mem = {}


def lcs_recursive(stra, strb, i, j):
    """
    An auxiliary recursive function for calculating
    the length of the longest common SUBSTRING (consecutive characters)
    ENDING at positions i-1 and j-1
    """
    if (i, j) in mem:
        return mem[(i, j)]

    if i == 0 or j == 0:
        mem[(i, j)] = 0
        return 0

    if stra[i - 1] == strb[j - 1]:
        result = 1 + lcs_recursive(stra, strb, i - 1, j - 1)
    else:
        result = 0

    mem[(i, j)] = result
    return result


def comp(a, b, m, n):
    """
    Finds the maximum length of a common SUBSTRING
    (consecutive characters) for strings a and b.
    """
    global mem
    mem = {}

    max_length = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            length = lcs_recursive(a, b, i, j)
            if length > max_length:
                max_length = length

    return max_length


print(comp('abxc', 'xbxc', 4, 4))
