"""
    来源：力扣（LeetCode）
    链接：https://leetcode.cn/problems/non-overlapping-intervals
    难度：中等
    解法：贪心算法
    题目描述：
    给定一个区间的集合intervals，其中 intervals[i] = [starti, endi]。返回需要移除区间的最小数量，
    使剩余区间互不重叠。

    Input_1: intervals = [[1,2],[2,3],[3,4],[1,3]]
    Output_1: 1
    Input_2: intervals = [[1,2], [1,2], [1,2]]
    Output_2: 2
    Input_2: intervals = [[1,2], [2,3]]
    Output_2: 0

"""

"""
    这里先按照右端进行升序排序，思想类似于，如果想在一段时间内安排更多次数的会议，我们优先安排较早结束的，早结束的不会影响
    晚结束的，有一点像题目406矮个子插队到高个子前面。有一些疑惑的地方在于，比如输入是[[1,2],[1,3],[3,4]]，按照做法是把[1,2]
    作为首区间，但是其实把[1,3]作为首区间也是可以的，但是不影响我们要删除的数量
"""


# Leetcode版
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        prev = intervals[0][1]
        remove = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < prev:
                remove += 1
            else:
                prev = intervals[i][1]
        return remove


# ACM版
"""
    大概率在输入时要先输入一个N，代表区间的个数
"""
while True:
    try:
        n = int(input())
        intervals = []
        for i in range(n):
            s = list(map(int, input().split()))
            intervals.append(s)
        intervals.sort(key=lambda x: x[1])
        prev = intervals[0][1]
        remove = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < prev:
                remove += 1
            else:
                prev = intervals[i][1]
        print(remove)

    except:
        break
