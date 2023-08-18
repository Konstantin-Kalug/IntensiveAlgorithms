from typing import List


def bubble_sort(array: List[int]) -> List[int]:
    for i in range(len(array)):
        for j in range(len(array) - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


# https://leetcode.com/problems/sort-colors/description/
