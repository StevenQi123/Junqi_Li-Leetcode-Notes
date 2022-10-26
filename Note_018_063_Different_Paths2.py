"""
    来源：力扣（LeetCode）
    链接：https://leetcode.cn/problems/unique-paths-ii
    难度：中等
    解法：动态规划
    题目描述：
    一个机器人位于一个m x n网格的左上角 （起始点在下图中标记为 “Start” ）。机器人每次只能向下或者向右移动一步。
    机器人试图达到网格的右下角（在下图中标记为 “Finish”）。现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
    网格中的障碍物和空位置分别用 1 和 0 来表示。

    Input_1: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
    Output_1: 2
    Input_2: obstacleGrid = [[0,1],[0,0]]
    Output_2: 1

"""

"""
    和Leetcode062基本一致，区别在进行初始化时，一旦有障碍，就令有障碍的格子的路径为0
    
"""


# Leetcode版
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        matrix = [[0 for i in range(n)] for i in range(m)]
        if obstacleGrid[0][0] == 1:
            return 0
        matrix[0][0] = 1
        for i in range(1, m):
            if obstacleGrid[i][0] == 1:
                matrix[i][0] = 0
            else:
                matrix[i][0] = matrix[i - 1][0]
        for j in range(1, n):
            if obstacleGrid[0][j] == 1:
                matrix[0][j] = 0
            else:
                matrix[0][j] = matrix[0][j - 1]
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]
        return matrix[m - 1][n - 1]


# ACM版
while True:
    try:
        n = int(input())
        obstacleGrid = []
        for i in range(n):
            obstacleGrid.append(list(map(int, input().split())))
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        matrix = [[0 for i in range(n)] for i in range(m)]
        if obstacleGrid[0][0] == 1:
            print(0)
        matrix[0][0] = 1
        for i in range(1, m):
            if obstacleGrid[i][0] == 1:
                matrix[i][0] = 0
            else:
                matrix[i][0] = matrix[i - 1][0]
        for j in range(1, n):
            if obstacleGrid[0][j] == 1:
                matrix[0][j] = 0
            else:
                matrix[0][j] = matrix[0][j - 1]
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]
        print(matrix[m - 1][n - 1])
    except:
        break
