# 题目描述
# 哦，不！你不小心把一个长篇文章中的空格、标点都删掉了，并且大写也弄成了小写。像句子
# "I reset the computer. It still didn’t boot!"已经变成了"iresetthecomputeritstilldidntboot"。在处理标点符号和大小写之前，
# 你得先把它断成词语。当然了，你有一本厚厚的词典dictionary，不过，有些词没在词典里。假设文章用sentence表示，设计一个算法，
# 把文章断开，要求未识别的字符最少，返回未识别的字符数。
# 注意：本题相对原题稍作改动，只需返回未识别的字符数
#
# 示例：
# 输入：
# dictionary = ["looked","just","like","her","brother"]
# sentence = "jesslookedjustliketimherbrother"
# 输出： 7
# 解释： 断句后为"jess looked just like tim her brother"，共7个未识别字符。
#
# 提示：
# 0 <= len(sentence) <= 1000
# dictionary中总字符数不超过 150000。
# 你可以认为dictionary和sentence中只包含小写字母。
#
# 同样是看题解的一天，虽然想到了要使用动态规划，但是没有准确定义子问题及状态转移函数，所以看了题解。
#
# 子问题定义：
#   dp[i] 表示到所给字符串的第i个字符时未识别的字符数量。
# 转移函数定义：
#  我们考虑从第j(j<i)个字符开始到第i个字符构成的子串能够被识别。如果不能被识别，则dp[i] = dp[i - 1] + 1;
#  如果能被识别，那么dp[i] = dp[i - j]。
#
# 同时我们需要对字典中所有单词进行匹配，并且要保证未识别的字符数量最少
# 这里有一点需要注意，我们在匹配的时候时间效率并没有达到很好，对某些子串我们可以确定它不是任一单词的后缀，但我们还是遍历
# 了所有的单词，这就降低了时间效率。
# 改进方式是使用字典树来判断当前子串是否是单词的后缀。如果不是，则跳出循环。


class Solution:
    def respace(self, dictionary: list[str], sentence: str) -> int:
        dictionary = set(dictionary)
        size = len(sentence) + 1
        dp = [0] * size

        for i in range(1, size):
            dp[i] = dp[i-1] + 1
            for word in dictionary:
                k = len(word)
                if i >= k :
                    t = dp[i-k] if sentence[i-k:i] == word else dp[i-k]+k
                    dp[i] = min(dp[i], t)
        return dp[-1]
