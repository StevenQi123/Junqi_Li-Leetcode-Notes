"""

    来源：力扣（LeetCode）
    链接：https://leetcode.cn/problems/fibonacci-number
    难度：简单
    解法：递归
    题目描述：
    斐波那契数（通常用 F(n)表示）形成的序列称为斐波那契数列 。该数列由 0和 1开始，后面的每一项数字都是前面两项数字的和。也就是：
    F(0) = 0，F(1) = 1
    F(n) = F(n - 1) + F(n - 2)，其中 n > 1
    给定n ，请计算 F(n) 。

    Input_1: n=3
    Output_1: 2

"""

# Leetcode版
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        dp = [0,1]
        for i in range(n-1):
            dp.append(dp[-1]+dp[-2])
        return dp[-1]

# ACM版
while True:
    try:
        n = int(input())
        if n <= 1:
            print(n)
        dp = [0,1]
        for i in range(n-1):
            dp.append(dp[-1]+dp[-2])
        print(dp[-1])

    except:
        break