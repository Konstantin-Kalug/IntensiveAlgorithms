from typing import List


def prime_numbers(n: int) -> List[int]:
    return


# https://leetcode.com/problems/count-primes/
def prime_numbers(n: int) -> List[int]:
    array = [i for i in range(2, n)]
    num = 2
    j = 0
    while num <= int(n ** 0.5):
        i = j + 1
        while i != len(array):
            if array[i] % num == 0 and array[i] != num:
                del array[i]
            else:
                i += 1
        j += 1
        num = array[j]
    return len(array)