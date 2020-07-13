# 题目描述 不同路径 II
# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
# 现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
# 网格中的障碍物和空位置分别用 1 和 0 来表示。
# 说明：m 和 n 的值均不超过 100。
#
# 示例 1:
# 输入:
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# 输出: 2
# 解释:
# 3x3 网格的正中间有一个障碍物。
# 从左上角到右下角一共有 2 条不同的路径：
# 1. 向右 -> 向右 -> 向下 -> 向下
# 2. 向下 -> 向下 -> 向右 -> 向右
#
# 机器人只能向下和向右移动，那么，第一行的每一个格子就只能由其左边的格子到达，第一列的格子则是由其上方的格子到达。考虑到
# 有障碍，那么我们考虑转移函数：
# 如果obstacleGrid[0][i] 有障碍，那么就不能到达，则为0条路径；如果没有障碍，则是到达obstacleGrid[0][i-1]的路径数量。
# 同理，我们可以对第一列进行相同的处理。那么，到达其余格子的路径数量的转移函数呢？
# 我们直到机器人只能向下或者向右移动，那么到达当前格子则只能是从左边或者上边的格子前进一步，到达当前格子。由此，我们可以
# 定义出转移函数：
# 如果obstacleGrid[0][i] 有障碍，那么就不能到达，则为0条路径；如果没有障碍，则是到达obstacleGrid[i][j-1]的路径数量 +
# 到达obstacleGrid[i - 1][j]的路径数量。
# 需要注意的是，一开始就有障碍的情况，即输入为[[1]].

class Solution:
    # def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 0:
            obstacleGrid[0][0] = 1
        else:
            return 0
        for i in range(1, n):
            obstacleGrid[0][i] = obstacleGrid[0][i - 1] if obstacleGrid[0][i] == 0 else 0
        for j in range(1, m):
            obstacleGrid[j][0] = obstacleGrid[j - 1][0] if obstacleGrid[j][0] == 0 else 0
        for i in range(1, m):
            for j in range(1,n):
                obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1] if obstacleGrid[i][j] == 0 else 0
        return obstacleGrid[m-1][n-1]