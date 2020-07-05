# 题目描述 通配符匹配
# 给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。
# '?' 可以匹配任何单个字符。
# '*' 可以匹配任意字符串（包括空字符串）。
# 两个字符串完全匹配才算匹配成功。
# 说明:
# s 可能为空，且只包含从 a-z 的小写字母。
# p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。

# 示例 1:
# 输入:
# s = "aa"
# p = "a"
# 输出: false
# 解释: "a" 无法匹配 "aa" 整个字符串。

# 示例 2:
# 输入:
# s = "aa"
# p = "*"
# 输出: true
# 解释: '*' 可以匹配任意字符串。

# 示例 3:
# 输入:
# s = "cb"
# p = "?a"
# 输出: false
# 解释: '?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。

# 示例 4:
# 输入:
# s = "adceb"
# p = "*a*b"
# 输出: true
# 解释: 第一个 '*' 可以匹配空字符串, 第二个 '*' 可以匹配字符串 "dce".

# 示例 5:
# 输入:
# s = "acdcb"
# p = "a*c?b"
# 输出: false

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # n = len(p)
        # picked = [[] for _ in range(n)]
        # #一个字符的匹配
        # if s[0] == p[0] or p[0] == '?':
        #     picked[0].append(s[0])
        # # "*" 可以匹配任意字符
        # elif p[0] == '*':
        #     picked[0].append('') # 添加空字符
        #     for i in range(0,len(s)):
        #         picked[0].append(s[:i+1])
        #
        # for i in range(1, n):
        #     if p[i] != '?' and p[i] != '*':
        #         for j in range(len(picked[i - 1])):
        #             pick = picked[i-1][j] + p[i]
        #             if pick in s:
        #                 picked[i].append(pick)
        #     elif p[i] == '?':
        #         for j in range(len(picked[i - 1])):
        #             if picked[i - 1][j] != '':
        #                 index = s.index(picked[i - 1][j]) + len(picked[i - 1][j])
        #                 if index >= len(s):
        #                     continue
        #                 pick = picked[i - 1][j] + s[index]
        #                 picked[i].append(pick)
        #             else:
        #                 picked[i].append(s[0])
        #     else:
        #         for j in range(len(picked[i - 1])):
        #             index = 0
        #             if picked[i - 1][j] != '':
        #                 index = s.index(picked[i - 1][j]) + len(picked[i - 1][j])
        #             if index > len(s):
        #                 continue
        #             ms = 0
        #             for m in range(index, len(s) + 1):
        #                 pick = picked[i - 1][j] + s[index:m]
        #                 picked[i].append(pick)
        #                 ms += 1
        # for i in range(len(picked)):
        #     print(picked[i])
        #
        # if len(picked[n - 1]) != 0 and picked[n - 1][len(picked[n-1]) - 1] == s:
        #     return True
        # else:
        #     return False
        m, n = len(s), len(p)

        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for i in range(1, n + 1):
            if p[i - 1] == '*':
                dp[0][i] = True
            else:
                break

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 1] | dp[i - 1][j]
                elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]

        return dp[m][n]

if __name__ == "__main__":
    so = Solution()
    an = so.isMatch("aaaa","***a")
    print(an)

