"""
    来源：力扣（LeetCode）
    链接：https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iii
    难度：困难
    解法：动态规划
    题目描述：
    给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。设计一个算法来计算你所能获取的最大利润。
    你最多可以完成两笔交易。注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

    Input_1: prices = [3,3,5,0,0,3,1,4]
    Output_1: 6
    Input_2: prices = [1,2,3,4,5]
    Output_2: 4

"""

"""
    这道题难就难在该怎么定义”状态“，用简单的dp二维数组根本无法代表状态，这里参考leetcode官方给出的思路，
    既然有两次买卖，那么任意一天，我们都有可能处于4种不同的状态：第一次买buy1，第一次卖sell1，第二次买bu2，
    第二次卖sell2。为什么要这样定义状态，因为处在任何一天，都有可能是在这4种状态之中，牵一发而动全身，尽管
    会计算很多东西，但是这个问题就是这么复杂，任何新的一天的加入，都有可能影响2次买卖中的任何一次。接下来看
    状态是如何转移的。假设buy1,buy2,sell1,sell2代表四种状态下，当天的最大利润，buy1[i] = max(buy1[i-1],
    -price[i]),sell1[i] = max(sell1[i-1],price[i]+buy1[i-1]),buy2 = max(buy2[i-1],sell1[i-1]
    -price[i]),sell2[i] = max(sell2[i-1],price[i]+buy2[i-1])。这里buy2比较难理解，如果根本不需要
    第二次买卖操作就能获取最大值，那么说明，当前第二次买的价格是大于等于第一次卖的价格的
"""

# Leetcode版
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy_1 = -prices[0]
        sell_1 = 0
        buy_2 = -prices[0]
        sell_2 = 0
        for i in range(1, n):
            buy_1 = max(buy_1, -prices[i])
            sell_1 = max(sell_1, prices[i] + buy_1)
            buy_2 = max(buy_2, sell_1 - prices[i])
            sell_2 = max(sell_2, prices[i] + buy_2)

        return sell_2