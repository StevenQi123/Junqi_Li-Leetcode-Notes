"""
    来源：力扣（LeetCode）
    链接：https://leetcode.cn/problems/shortest-bridge/description
    难度：中等
    解法：dfs+bfs
    题目描述：
    给你一个大小为 n x n的二元矩阵 grid ，其中1表示陆地，0表示水域。岛是由四面相连的1形成的一个最大组，
    即不会与非组内的任何其他1相连。grid中恰好存在两座岛。你可以将任意数量的0变为 1，以使两座岛连接起来,
    变成一座岛。返回必须翻转的 0 的最小数目。

    Input_1: grid = [[0,1],[1,0]]
    Output_1: 1
    Input_2: grid = [[0,1,0],[0,0,0],[0,0,1]]
    Output_2: 2

"""


from collections import deque
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            q.append((i,j))
            grid[i][j] = 2
            for dx, dy in dic:
                x = i + dx
                y = j + dy
                if 0 <= x < n and 0 <= y < n and grid[x][y] == 1:
                    dfs(x, y)

        n = len(grid)
        dic = ((0, 1), (1, 0), (-1, 0), (0, -1))
        q = deque()
        # 找到一个陆地
        for i, row in enumerate(grid):
            for j, c in enumerate(row):
                if grid[i][j] == 1:
                    q.append((i, j))
                    break
            if q:
                break

        # 通过深度优先搜索将这个岛全部染色
        i, j = q[0]
        dfs(i, j)
        res = 0
        # 接下来广度优先搜索
        while True:
            for __ in range(len(q)):
                i, j = q.popleft()
                for dx, dy in dic:
                    x = i + dx
                    y = j + dy
                    if 0 <= x < n and 0 <= y < n:
                        if grid[x][y] == 1:
                            return res
                        elif grid[x][y] == 0:
                            grid[x][y] == 2
                            q.append((x, y))
            res += 1