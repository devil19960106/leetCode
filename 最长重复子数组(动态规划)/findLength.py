# 题目描述 最长重复子数组
# 给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。
# 示例：
# 输入：
# A: [1,2,3,2,1]
# B: [3,2,1,4,7]
# 输出：3
# 解释：
# 长度最长的公共子数组是 [3, 2, 1] 。
# 提示：
#
# 1 <= len(A), len(B) <= 1000
# 0 <= A[i], B[i] < 100
#dp[i][j] 表示 A[:i]与B[:j]的最长公共前缀长度
class Solution:
    def findLength(self, A, B):
        n, m = len(A), len(B)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        ans = 0
        for i in range(n):
            for j in range(m):
                dp[i][j] = dp[i - 1][j - 1] + 1 if A[i] == B[j] else 0
                ans = max(ans, dp[i][j])
        for i in range(n):
            print(dp[i])
        return ans

if __name__ == "__main__":
    so = Solution()
    an = so.findLength([1,2,3,2,1], [3,2,1,4,7])
    print(an)