from typing import List


def spiral_matrix(n: int) -> List[List[int]]:
    num = 1
    if n == 1:
        return [[1]]
    output = [[0 for _ in range(n)] for _ in range(n)]
    borders_j = [-1, n]
    borders_i = [-1, n]
    direction = 0
    i = 0
    j = 0
    k = 0
    while num <= n ** 2:
        if direction == 0:
            while j not in borders_j:
                if k == 0 and num != 1:
                    k = 1
                    borders_j.append(j)
                    j += 1
                    continue
                output[i][j] = num
                num += 1
                j += 1
                k = 1
            direction += 1
            j -= 1
            k = 0
        elif direction == 1:
            while i not in borders_i:
                if k == 0 and num != 1:
                    k = 1
                    borders_i.append(i)
                    i += 1
                    continue
                output[i][j] = num
                num += 1
                i += 1
            direction += 1
            i -= 1
            k = 0
        elif direction == 2:
            while j not in borders_j:
                if k == 0 and num != 1:
                    k = 1
                    borders_j.append(j)
                    j -= 1
                    continue
                output[i][j] = num
                num += 1
                j -= 1
            direction += 1
            j += 1
            k = 0
        elif direction == 3:
            while i not in borders_i:
                if k == 0 and num != 1:
                    k = 1
                    borders_i.append(i)
                    i -= 1
                    continue
                output[i][j] = num
                num += 1
                i -= 1
            direction = 0
            i += 1
            k = 0
    return output

print(spiral_matrix(3))
# https://leetcode.com/problems/spiral-matrix-ii/
