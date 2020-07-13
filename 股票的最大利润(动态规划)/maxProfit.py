# 题目描述
# 假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？
#
# 示例 1:
# 输入: [7,1,5,3,6,4]
# 输出: 5
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
#      注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
#
# 示例 2:
# 输入: [7,6,4,3,1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
# 限制：
# 0 <= 数组长度 <= 10^5
# 状态定义：
# profits[i] 表示第i天的最大利润
# 转移函数定义：
# 第1天的利润为0，第i天的利润为第i-1天的利润加上这两天股票的差值，如果利润小于0，则置为0

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        profits = [0 for _ in range(n)]
        maxProfit = 0
        for i in range(1, n):
            profits[i] = max(0, prices[i] - prices[i - 1] + profits[i - 1])
            maxProfit = max(maxProfit, profits[i])
        return maxProfit