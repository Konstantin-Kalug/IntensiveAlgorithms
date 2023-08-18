from typing import List


def binary_search(value: int, array: List[int]) -> int:
    l, r = 0, len(array)
    while l < r:
        m = (l + r + 1) // 2
        if array[m] > value:
            r = m - 1
        elif array[m] < value:
            l = m
        else:
            l = m
            break
    return l - 1


# https://leetcode.com/problems/binary-search/
# https://leetcode.com/problems/search-insert-position/
