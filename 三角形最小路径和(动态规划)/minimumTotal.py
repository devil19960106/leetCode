# 题目描述
# 给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
# 相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。
# 例如，给定三角形：
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# 自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
# 说明：
# 如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。

# 自上而下
# 子状态定义：
# path[i][j] 表示从顶层到第i层的第j个节点的路径最小路径和
# 转移函数：
# path[i][j] = min(path[i - 1][j], path[i - 1][j - 1]) + triangle[i][j]
# 考虑边界情况，，即j == 0 时，path[i][0] 只能由path[i - 1][0] 转移而来；
# 而当j == i时，path[i][j] 只能1由path[i - 1][i - 1]转移而来。

# 自下而上：
# 从倒数第二层开始，修改原数组，状态转移函数为：
# triangle[i - 1][j] += min(triangle[i][j], triangle[i][j + 1])

class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        # 自上而下
        # n = len(triangle)
        # path = [[0] * n for _ in range(n)]
        # path[0][0] = triangle[0][0]

        # for i in range(1, n):
        #     path[i][0] = path[i - 1][0] + triangle[i][0]
        #     for j in range(1, i):
        #        path[i][j] = min(path[i - 1][j], path[i - 1][j - 1]) + triangle[i][j]
        #     path[i][i] = path[i - 1][i - 1] + triangle[i][i]

        # return min(path[n - 1])
        # 自下而上
        for i in range(len(triangle) - 1, 0, -1):
            for j in range(i):
                triangle[i - 1][j] += min(triangle[i][j], triangle[i][j + 1])
        return triangle[0][0]