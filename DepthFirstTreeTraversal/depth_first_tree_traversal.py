from typing import Dict
from typing import List


def depth_first_tree_traversal(root: int, tree: Dict[int, List[int]]) -> List[int]:
    output = []
    output.append(root)
    dfs(output, root, tree)
    return output[::-1]


def dfs(output, root, tree):
    for r in tree[root][::-1]:
        if r not in output and not (r is None):
            output.append(r)
            dfs(output, r, tree)


# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
