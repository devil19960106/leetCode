# 题目描述 连续子数组的最大和 动态规划
# 输入一个整型数组，数组里有正数也有负数。数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。
# 要求时间复杂度为O(n)。

# 示例1:
# 输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

# 提示：
# 1 <= arr.length <= 10^5
# -100 <= arr[i] <= 100

# 动态规划的题目最难的是子状态的定义，也就是要解决的子问题的定义，这个题定义的子状态为：
# “dp[i]为元素包含nums[i]的连续子数组的和的最大值”，状态转移函数为：
# 如果dp[i - 1] < 0 ，则说明前面的连续子数组对dp[i]的贡献是负的，所以dp[i] = nums[i];
# 如果dp[i - 1] > 0, 则dp[i] = dp[i - 1] + nums[i]

class Solution:
    def maxSubArray(self, nums):
        n = len(nums)
        for i in range(1,n):
            if nums[i - 1] <= 0:
                nums[i] = nums[i]
            else:
                nums[i] = nums[i] + nums[i - 1]
        return max(nums)

if __name__ == "__main__":
    so = Solution()
    an = so.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
    print(an)