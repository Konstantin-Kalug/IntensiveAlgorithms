from typing import Dict, Optional
from typing import List


def breadth_first_tree_traversal(root: int, tree: Dict[int, List[int]]) -> List[int]:
    """
    Completes breadth first tree traversal and returns visited vertices
    Go to left side of tree, then right, then self

    Args:
        root (int): root vertex
        tree (Dict[int, List[int]]): structure of tree
                            (number of vertex, list of two elements: child number or None)
    """

    return []


# https://leetcode.com/problems/binary-tree-level-order-traversal/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []
        self.bfs(root, output, 0)
        ans = []
        output = sorted(output, key=lambda x: x[1])
        for j in range(len(output)):
            if output[j][1] == len(ans) - 1:
                ans[-1] += output[j][0]
            else:
                ans.append(output[j][0])
        return ans

    def bfs(self, root, output, i):
        if root is None:
            return
        if len(output) == 0:
            output.append(([root.val], i))
            i += 1
        preoutput = []
        if root.left is not None:
            preoutput.append(root.left.val)
        if root.right is not None:
            preoutput.append(root.right.val)
        if len(preoutput) != 0:
            output.append((preoutput, i))
        if root.left is not None:
            self.bfs(root.left, output, i + 1)
        if root.right is not None:
            self.bfs(root.right, output, i + 1)
