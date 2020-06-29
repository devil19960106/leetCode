# 题目描述
# 给定一个有序整数数组，元素各不相同且按升序排列，编写一个算法，创建一棵高度最小的二叉搜索树。
# 示例:
# 给定有序数组: [-10,-3,0,5,9],
# 一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：
#
#           0
#          / \
#        -3   9
#        /   /
#      -10  5
# 方法：由于是升序的数组，想要构建的二叉搜索树高度最小，那么就要避免在最后一层之前出现空节点的情况。二叉搜索树的特点是
# 左子树<根<右子树，那么我们可以知道，数组的中位数必然是树的根节点，前面部分为左子树，后面部分为右子树。这样重复上述划分，
# 直到数组为空，结束递归。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode:
        if not len(nums):
            return
        mid = len(nums) // 2
        root_val = nums[mid]
        root = TreeNode(root_val)
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        return root