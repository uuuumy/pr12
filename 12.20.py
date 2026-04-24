mem = {}

def lcs_recursive(stra, strb, i, j):
    """
    An auxiliary recursive function for calculating
    the length of the longest common subsequence
    """
    if (i, j) in mem:
        return mem[(i, j)]

    if i == 0 or j == 0:
        mem[(i, j)] = 0
        return 0

    if stra[i - 1] == strb[j - 1]:
        result = 1 + lcs_recursive(stra, strb, i - 1, j - 1)
    else:
        result = max(lcs_recursive(stra, strb, i - 1, j),
                     lcs_recursive(stra, strb, i, j - 1))

    mem[(i, j)] = result
    return result

def comp(a, b, m, n):
    """
    Finds the maximum length of a common
    subsequence of characters for strings a and b.
    """
    global mem
    mem = {}
    return lcs_recursive(a, b, m, n)

print(comp('abcde', 'ace', 5, 3))
