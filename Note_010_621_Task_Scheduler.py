import collections
"""
    来源：力扣（LeetCode）
    链接：https://leetcode.cn/problems/task-scheduler
    难度：中等
    解法：贪心算法
    题目描述：
    给你一个用字符数组tasks表示的CPU需要执行的任务列表。其中每个字母表示一种不同种类的任务。任务可以以任意顺序执行，
    并且每个任务都可以在1个单位时间内执行完。在任何一个单位时间，CPU可以完成一个任务，或者处于待命状态。然而，两个相同种类
    的任务之间必须有长度为整数n的冷却时间，因此至少有连续n个单位时间内CPU在执行不同的任务，或者在待命状态。你需要计算完成所
    有任务所需要的最短时间 。

    Input_1：tasks = ["A","A","A","B","B","B"], n = 2
    Output_1：8
    Input_2：tasks = ["A","A","A","B","B","B"], n = 0
    Output_2：6

"""

"""
    这道题的思路很奇妙，我们首先统计出现最多次的任务A的次数num_A，由于每一个同样任务要间隔n,那么至少需要
    num_A-1 * n + num_1的时间，相当于插空，A 0 0 A 0 0 A...，只有一种情况在最后一个A后面还有任务，那就是
    有任务出现次数和A一样多，这时候统计这些任务的类别数加上去就行。当n=0时，这个公式计算出来的时间会小于任务数。
    
"""


# Leetcode版
# class Solution:
#     def leastInterval(self, tasks: List[str], n: int) -> int:
#         T = dict(collections.Counter(tasks))
#         T = sorted(T.items(),key = lambda x:x[1],reverse = True)
#         max_char = T[0][1]
#         time = (max_char-1)*n + max_char
#         for i in range(1,len(T)):
#             if T[i][1] == max_char:
#                 time += 1
#         time = max(time,len(tasks))
#         return time

# ACM版
while True:
    try:
        s = list(input().split())[0]
        tasks = []
        for i in range(len(s)):
            tasks.append(s[i])
        n = int(input())
        T = dict(collections.Counter(tasks))
        T = sorted(T.items(), key=lambda x: x[1], reverse=True)
        max_char = T[0][1]
        time = (max_char - 1) * n + max_char
        for i in range(1, len(T)):
            if T[i][1] == max_char:
                time += 1
        time = max(time, len(tasks))
        print(time)

    except:
        break
