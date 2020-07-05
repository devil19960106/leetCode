# 题目描述  判断子序列
# 给定字符串 s 和 t ，判断 s 是否为 t 的子序列。
# 你可以认为 s 和 t 中仅包含英文小写字母。字符串 t 可能会很长（长度 ~= 500,000），而 s 是个短字符串（长度 <=100）。
# 字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"
# 的一个子序列，而"aec"不是）。
#
# 示例 1:
# s = "abc", t = "ahbgdc"
# 返回 true.
#
# 示例 2:
# s = "axc", t = "ahbgdc"
# 返回 false.
# dp[i] 表示s中第i个字符的匹配位置

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        if n == 0 and m == 0:
            return True
        elif m == 0:
            return False
        elif n == 0 and m != 0:
            return True
        dp = [0] * n
        index = t.find(s[0])
        if index != -1:
            index = index + 1
            dp[0] = index
            t = t[index:]
        else:
            return False
        for i in range(1, n):
            index = t.find(s[i])
            if index != -1:
                index = index + 1
                dp[i] = dp[i - 1] + index
                t = t[index:]
            else:
                return False
        return True

if __name__ == "__main__":
    so = Solution()
    an = so.isSubsequence("axc", "ahbgdc")
    print(an)