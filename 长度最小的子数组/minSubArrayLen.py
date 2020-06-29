# 题目描述
# 给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组，并返回其长度。
# 如果不存在符合条件的连续子数组，返回 0。
#
# 示例:
# 输入: s = 7, nums = [2,3,1,2,4,3]
# 输出: 2
# 解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
#
# 进阶:
# 如果你已经完成了O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。
# 方法1：
# 暴力解决这个问题，从窗口大小为1开始遍历数组，如找到一个子数组大于给定的数s则结束；否则增大窗口，再次遍历。如果当窗口大
# 小达到数组的长度还是没能找到则返回0。
# 思路没问题，时间复杂度为O(n^2)，python超时了。
# 方法2：
# 使用两个指针，start，end。end的作用是用来寻找满足 >= s的子数组，start的作用是在满足条件的子数组中寻找最小的。
# 首先，都从数组的开始位置进行遍历，end遍历，直到找到一个满足条件的子数组。然后start开始遍历，这时比较end - start + 1与
# 最小子数组长度，变更最小子数组长度。直到end走到数组结尾。
class Solution:
    def minSubArrayLen(self, s, nums):
        index = 1
        while index <= len(nums):
            for i in range(len(nums)):
                add = sum(nums[i:index + i])
                if add >= s:
                    return index
            index += 1
        return 0

class Solution_2:
    def minSubArrayLen(self, s, nums):
        start, end = 0, 0
        min_len = len(nums) + 1
        add = 0
        while end < len(nums):
            add += nums[end]
            while add >= s:
                add -= nums[start]
                min_len = min(min_len, end - start + 1)
                start += 1
            end += 1
        return 0 if min_len == (len(nums) + 1) else min_len