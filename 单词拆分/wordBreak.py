# 题目描述
# 给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。
# 说明：
# 拆分时可以重复使用字典中的单词。
# 你可以假设字典中没有重复的单词。
# 示例 1：
# 输入: s = "leetcode", wordDict = ["leet", "code"]
# 输出: true
# 解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
# 示例 2：
# 输入: s = "applepenapple", wordDict = ["apple", "pen"]
# 输出: true
# 解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
#      注意你可以重复使用字典中的单词。
# 示例 3：
# 输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出: false


# 动态规划的题目 自己想了一些方法但都无法AC,所以看了题解，然后又去看了动态规划
# 动态规划的思路大致是这样的：
# 现有一个问题，它的解能够有它的子问题的解来表示，那么我们就可以将问题分解为它的子问题来求解，继续分解，最终
# 我们可以得到一个初始的解。然后求解问题的方式有两种：
# 1.自顶向下的方法
# 2.自底向上的方法

# 第一种方法 暂时没懂
# 第二种方法 从最小的子问题还是求解，直到完成问题的解答。
# 首先生成一个列表dp[],dp[i]表示字符串s中前i个字符能否被字典中的词匹配，例如"leetcode", ['leet', 'code']
# 空的情况为Ture, ‘l’不能匹配，为False，直到‘leet'匹配，所以，到这里的匹配情况为
# [Ture, False, False, False, Ture],继续往后遍历，直到结束，最后的结果为：
# [Ture, False, False, False, Ture, False, False, False, Ture]
# 这里需要说明一下dp[i]的判定：
# 我们将s[0,..,i]分成两个部分s1 = s[0,..,j]和s2 = s[j,...,i-1],分别判断s1和s2是否能够匹配，s1是前j个字符的匹配情况，
# 由于我们是从最小的子问题开始求解的，所以dp[j]我们已经计算过了，现在需要判断s2是否能够匹配，如果能，则dp[i]为Ture,
# 不能，则为False.


class Solution:
    def wordBreak(self, s, wordDict):
        n = len(s) + 1
        dp = [False] * n
        dp[0] = True
        for i in range(1, n):
            for j in range(i - 1, -1, -1):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]

class Solution_2:
    def wordBreak(self, s, wordDict):
        n = len(s) + 1
        dp = [False] * n
        maxlen = 0
        for word in wordDict:
            maxlen = max(maxlen, len(word))
        dp[0] = True
        for i in range(1, n):
            temp = i - maxlen
            for j in range(i - 1, temp -1, -1):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]

class Solution_3:
    def wordBreak(self, s, wordDict):
        dp = {}
        wordDict = set(wordDict)
        def dfs(s1):
            if s1 in dp:
                return dp[s1]
            for word in wordDict:
                if s1 == word:
                    return True
                if s1.startswith(word):
                    ans = dfs(s1[len(word):])
                    dp[s1] = ans
                    if ans:
                        return True
            return False
        return dfs(s)

if __name__ == "__main__":
    so = Solution_3()
    an = so.wordBreak("leetcode",
["leet","code"])
    print(an)
