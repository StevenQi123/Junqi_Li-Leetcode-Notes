"""
    来源：力扣（LeetCode）
    链接：https://leetcode.cn/problems/climbing-stairs
    难度：简单
    解法：递归/动态规划
    题目描述：
    假设你正在爬楼梯。需要n阶你才能到达楼顶。每次你可以爬1或2个台阶。你有多少种不同的方法可以爬到楼顶呢？

    Input_1: n = 2
    Output_1: 2
    Input_2: n = 3
    Output_2: 3

"""

"""
    递归的思想，我们需要找到状态转移方程，这道题中，每一个台阶，有两种方法登上去，一种是由前一个台阶登一级，一种是
    由前前一个台阶登两级，所以对于每一个台阶，他登上来的方法由前面两个台阶的数量相加而得。我们知道当n=1,只有1种方
    法，所以我们为了处理边界，不如令dp=[0,1]，这样子每次数组最后两位相加添加到数组末尾，末尾的数就是方法的数量，例
    如，对于n =1 = 0 + 1, n = 2 = 1+1。

"""


# Leetcode版
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0, 1]
        for i in range(n):
            dp.append(dp[-1] + dp[-2])
        return dp[-1]


# ACM版
while True:
    try:
        n = int(input())
        dp = [0, 1]
        for i in range(n):
            dp.append(dp[-1] + dp[-2])
        print(dp[-1])

    except:
        break
