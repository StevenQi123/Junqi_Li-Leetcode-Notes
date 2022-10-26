"""
    来源：力扣（LeetCode）
    链接：https://leetcode.cn/problems/unique-paths
    难度：中等
    解法：动态规划
    题目描述：
    一个机器人位于一个 m x n网格的左上角 （起始点在下图中标记为 “Start” ）。机器人每次只能向下或者向右移动一步。
    机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。问总共有多少条不同的路径？

    Input_1: m = 3, n = 7
    Output_1: 28
    Input_2: m = 3, n = 2
    Output_2: 3

"""

"""
    状态转移方程为dp[i][j] = dp[i-1][j] + dp[i][j-1]，初始化时，第一列和第一行全部为1

"""


# Leetcode版
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [[0 for i in range(n)] for i in range(m)]
        matrix[0][0] = 1
        for i in range(1, m):
            matrix[i][0] = 1
        for j in range(1, n):
            matrix[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]
        return matrix[m - 1][n - 1]


# ACM版
while True:
    try:
        m = int(input())
        n = int(input())
        matrix = [[0 for i in range(n)] for i in range(m)]
        matrix[0][0] = 1
        for i in range(1, m):
            matrix[i][0] = 1
        for j in range(1, n):
            matrix[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]
        print(matrix[m - 1][n - 1])

    except:
        break
