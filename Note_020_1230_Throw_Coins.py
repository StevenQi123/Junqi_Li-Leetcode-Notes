"""
    来源：力扣（LeetCode）
    链接：https://leetcode.cn/problems/toss-strange-coins
    难度： 中等
    解法：动态规划
    题目描述：
    有一些不规则的硬币。在这些硬币中，prob[i]表示第i枚硬币正面朝上的概率。请对每一枚硬币抛掷一次，
    然后返回正面朝上的硬币数等于target的概率。

    Input_1: prob = [0.4], target = 1
    Output_1: 0.40000
    Input_2: prob = [0.5,0.5,0.5,0.5,0.5], target = 0
    Output_2: 0.03125


"""

"""
    这道题是隐藏比较好的01背包问题，首先dp数组的含义很难想到，dp[i][j]代表了，使用i枚硬币，有j枚正面朝上的概率，
    那么我们的状态转移方程就有：1.第i枚朝上，前面i-1枚有j-1枚朝上；2.第i枚朝下，前面i-1枚有j枚朝上。那么我们可以
    写出方程：dp[i][j] = dp[i-1][j-1]*prob[i]+dp[i-1][j]*(1-prob[i])，然后要注意的是，prob数组与dp数组的
    索引是相差1的，因为我们所说的第一枚硬币，在索引中是第0个，我们在构建dp数组时就应当发现要把长度和宽度都扩大1，所以
    dp[i][j] = dp[i-1][j-1]*prob[i-1]+dp[i-1][j]*(1-prob[i-1])
    
"""

# Leetcode版
class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        n = len(prob)
        if n < target:
            return 0
        dp = [[0] * (target+1) for __ in range(n+1)]
        dp[0][0] = 1
        for i in range(1,n+1):
            dp[i][0] = (1-prob[i-1])*dp[i-1][0]
        for i in range(1,n+1):
            for j in range(1,target+1):
                dp[i][j] = dp[i-1][j-1]*prob[i-1] + dp[i-1][j]*(1-prob[i-1])
        return dp[n][target]