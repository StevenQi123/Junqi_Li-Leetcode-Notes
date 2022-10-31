"""
    来源：力扣（LeetCode）
    链接：https://leetcode.cn/problems/bomb-enemy
    难度：中等
    解法：动态规划
    题目描述：
    给你一个大小为 m x n 的矩阵 grid ，其中每个单元格都放置有一个字符：'W'表示一堵墙，'E'表示一个敌人
    '0'（数字 0）表示一个空位返回你使用一颗炸弹可以击杀的最大敌人数目。你只能把炸弹放在一个空位里。由于炸
    弹的威力不足以穿透墙体，炸弹只能击杀同一行和同一列没被墙体挡住的敌人。

    Input_1: grid = [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]
    Output_1: 3
    Input_2: grid = [["W","W","W"],["0","0","0"],["E","E","E"]]
    Output_2: 1

"""

# Leetcode版（会超时），不超时的思想是，不调用额外函数，直接更新一个二维数组
def maxKilledEnemies(grid) -> int:
    def my_count(x, y):
        res = 0
        for i in range(x - 1, -1, -1):
            if grid[i][y] == 'W':
                break
            if grid[i][y] == 'E':
                res += 1
        for i in range(x + 1, line, 1):
            if grid[i][y] == 'W':
                break
            if grid[i][y] == 'E':
                res += 1
        for i in range(y - 1, -1, -1):
            if grid[x][i] == 'W':
                break
            if grid[x][i] == 'E':
                res += 1
        for i in range(y + 1, col, 1):
            if grid[x][i] == 'W':
                break
            if grid[x][i] == 'E':
                res += 1
        print(x,y,res)
        return res

    res = 0
    line = len(grid)
    col = len(grid[0])
    for i in range(line):
        for j in range(col):
            if grid[i][j] == '0':
                res = max(res, my_count(i, j))
    return res

# 由于会超时这里就不做ACM版了
