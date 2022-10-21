"""
    来源：力扣（LeetCode）
    链接：https://leetcode.cn/problems/minimum-number-of-arrows-to-burst-balloons
    难度：中等
    解法：贪心算法
    题目描述：
    有一些球形气球贴在一堵用 XY 平面表示的墙面上。墙面上的气球记录在整数数组points，其中points[i] = [xstart, xend]
    表示水平直径在xstart和xend之间的气球。你不知道气球的确切y坐标。一支弓箭可以沿着x轴从不同点完全垂直地射出。在坐标x处
    射出一支箭，若有一个气球的直径的开始和结束坐标为 xstart，xend，且满足 xstart≤ x ≤ xend，则该气球会被引爆。可以射
    出的弓箭的数量没有限制 。弓箭一旦被射出之后，可以无限地前进。给你一个数组 points ，返回引爆所有气球所必须射出的最小
    弓箭数。

    Input_1: points = [[10,16],[2,8],[1,6],[7,12]]
    Output_1: 2
    Input_1: points = [[1,2],[3,4],[5,6],[7,8]]
    Output_1: 4

"""

"""
    和Leetcode435十分类似，要注意的点在于如果找到重叠的部分，要不断缩小右区间的范围
"""

# Leetcode版
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x:x[1])
        prev = points[0][1]
        n = 1
        for i in range(1,len(points)):
            if points[i][0] > prev:
                n+= 1
                prev = points[i][1]
            else:
                prev = min(points[i][1],prev)
        return n

# ACM版
while True:
    try:
        n = int(input())
        points = []
        for i in range(n):
            s = list(map(int,input().split()))
            points.append(s)
        points.sort(key=lambda x: x[1])
        prev = points[0][1]
        n = 1
        for i in range(1, len(points)):
            if points[i][0] > prev:
                n += 1
                prev = points[i][1]
            else:
                prev = min(points[i][1], prev)
        print(n)

    except:
        break