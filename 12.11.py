def ind_maxlist(a):
    """
    A recursive function for finding the index of
    the maximum element in a list of integer elements.
    """
    if not a:
        raise ValueError("список пустой")

    if len(a) == 1:
        return 0

    max_idx = ind_maxlist(a[1:])
    max_idx += 1
    if a[0] >= a[max_idx]:
        return 0
    return max_idx

print(ind_maxlist([1, 8, 8, 7, 8]))  