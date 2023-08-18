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


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        new_tree = {}
        if k == 0:
            return [target.val]
        point = int(target.val)
        self.dfs1(root, new_tree)
        points = [target.val]
        output = []
        self.dfs2(new_tree, target.val, 0, k, points, output)
        return sorted(output, key=lambda x: -x)

    def dfs1(self, root, new_tree):
        if root.val is None:
            return
        if root.val not in new_tree:
            new_tree[root.val] = []
        if not (root.left is None):
            new_tree[root.val] += [root.left.val]
            new_tree[root.left.val] = [root.val]
        if not (root.right is None):
            new_tree[root.val] += [root.right.val]
            new_tree[root.right.val] = [root.val]
        if not (root.left is None):
            self.dfs1(root.left, new_tree)
        if not (root.right is None):
            self.dfs1(root.right, new_tree)

    def dfs2(self, tree, t, n, k, points, output):
        for r in tree[t]:
            if r not in points and not (r is None):
                points.append(r)
                if n + 1 == k:
                    output.append(r)
                else:
                    self.dfs2(tree, r, n + 1, k, points, output)