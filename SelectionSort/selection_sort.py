from typing import List


def selection_sort(array: List[int]) -> List[int]:
    for i in range(len(array)):
        min_a = min(array[i:])
        if min_a < array[i]:
            array[i], min_a = min_a, array[i]
    return array


# https://leetcode.com/problems/sort-colors/
