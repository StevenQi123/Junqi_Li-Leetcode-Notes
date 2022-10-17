"""
    来源：力扣（LeetCode）
    链接：https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii
    难度：中等
    解法：暴力法
    题目描述：
    给你一个整数数组 prices ，其中prices[i] 表示某支股票第 i 天的价格。
    在每一天，你可以决定是否购买和/或出售股票。你在任何时候最多只能持有一股股票。你也可以先购买，然后在同一天出售。
    返回你能获得的最大利润，

    Input_1：prices = [7,1,5,3,6,4]
    Output_1：7
    Input_2：prices = [1,2,3,4,5]
    Output_2：4
    Input_3：prices = [7,6,4,3,1]
    Output_3：0

"""

"""
    由于可以在同一天买卖，所以只要能赚我们就卖,但是如果限制交易次数，如Stock iii/iv，我们不能使用贪心算法
"""


# Leetcode版 双80+
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices) - 1):
            tmp = prices[i + 1] - prices[i]
            if tmp > 0:
                profit += tmp
        return profit


# ACM版
while True:
    try:
        # 输入部分
        prices = list(map(int, input().split()))
        profit = 0
        for i in range(len(prices) - 1):
            tmp = prices[i + 1] - prices[i]
            if tmp > 0:
                profit += tmp
        print(profit)

    except:
        break
