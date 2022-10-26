"""
    来源：力扣（LeetCode）
    链接：https://leetcode.cn/problems/coin-change
    难度：中等
    解法：动态规划
    题目描述：
    给你一个整数数组 coins，表示不同面额的硬币；以及一个整数amount，表示总金额。
    计算并返回可以凑成总金额所需的最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回-1 。
    你可以认为每种硬币的数量是无限的。

    Input_1: coins = [1, 2, 5], amount = 11
    Output_1: 3
    Input_2: coins = [2], amount = 3
    Output_2: -1

"""
"""
    举一个简单的例子来写状态方程，假设coins = [c1,c2,c3],则f(n) = min(f(n-c1),f(n-c2),f(n-c3))+1,f(0)= 0
    动态规划的本质就是暴力枚举！！！
"""


# Leetcode版
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        if dp[amount] != float('inf'):
            return dp[amount]
        else:
            return -1


# ACM版
while True:
    try:
        coins = list(map(int, input().split()))
        amount = int(input())
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        if dp[amount] != float('inf'):
            print(dp[amount])
        else:
            print(-1)
    except:
        break
