# 题目描述 路径总和||
# 给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。
# 说明: 叶子节点是指没有子节点的节点。
# 示例:
# 给定如下二叉树，以及目标和 sum = 22，
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
# 返回:
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]
# 是上一个题的升级版本，不仅要判断是否存在从根节点到叶子节点的和与给定的target值是否相等，还要将完整路径输出。
# 整体思路没有改变，还是深度优先遍历，只是，这一次传递的路径，而不是路径的和。到叶子节点时，我们在计算路径的和与给定的
# target值是否相等。如果相等，则保存路径。这里需要注意的一点是，我们只使用了一个target数组来保存路径，所以在回退的时候，
# 我们需要将已经处理的元素从路径中删除。
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> list[list[int]]:
        if not root:
            return []
        targets = []
        def DFS(root, target):
            if root.left == None and root.right == None:
                target_num = 0
                target.append(root.val)
                for i in range(len(target)):
                    target_num += target[i]
                if target_num == sum:
                    targets.append(target[:])
                target.pop()

            if root.left != None:
                target.append(root.val)
                lTarget = target
                DFS(root.left, lTarget)

            if root.right != None:
                target.append(root.val)
                rTarget = target
                DFS(root.right, rTarget)
            if target:
                target.pop()

        DFS(root, [])
        return targets
