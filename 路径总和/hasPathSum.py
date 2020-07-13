# 题目描述 路径总和
# 给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。
# 说明: 叶子节点是指没有子节点的节点。
# 示例: 
# 给定如下二叉树，以及目标和 sum = 22，
#
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \      \
#         7    2      1
# 返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。
# 深度优先遍历，到叶子节点时将从根节点到叶子节点的值的和相加，存储。遍历结束后，在存储和的数组中看是否有与给定的target值
# 相等的数组元素，如果没有，则返回Flase，有则返回True。
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        targets = []
        def DFS(root, target):
            if root.left == None and root.right == None:
                targets.append(target + root.val)
            if root.left != None:
                DFS(root.left, target + root.val)
            if root.right != None:
                DFS(root.right, target + root.val)
        DFS(root, 0)
        if sum in targets:
            return True
        else:
            return False
