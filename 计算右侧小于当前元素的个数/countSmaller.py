# 题目描述
# 给定一个整数数组 nums，按要求返回一个新数组 counts。数组 counts 有该性质： counts[i] 的值是  nums[i] 右侧小于 nums[i] 的元素的数量。

# 示例:
# 输入: [5,2,6,1]
# 输出: [2,1,1,0]
# 解释:
# 5 的右侧有 2 个更小的元素 (2 和 1).
# 2 的右侧仅有 1 个更小的元素 (1).
# 6 的右侧有 1 个更小的元素 (1).
# 1 的右侧有 0 个更小的元素.
# 从后往前遍历数组，对于当前元素nums[i]，在nums[i:]中进行插入排序确定比元素小的右侧元素数量
# 超时了 使用的是插入排序

class Solution:
    def countSmaller(self, nums: list[int]) -> list[int]:
        def insertSort(arr, start):
            m = len(arr) - 1
            tmp = arr[start]
            j = start + 1
            while j <= m and arr[j] >= tmp:
                arr[j - 1] = arr[j]
                j += 1
            arr[j - 1] = tmp
            return m - j + 1
        n = len(nums)
        dp = [0 for _ in range(n)]
        for i in range(n-2, -1, -1):
            j = i + 1
            dp[i] = insertSort(nums, i)
        return dp
