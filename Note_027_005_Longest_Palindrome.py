"""
    来源：力扣（LeetCode）
    链接：https://leetcode.cn/problems/longest-palindromic-substring
    难度：中等（个人觉得是困难）
    解法：动态规划
    题目描述：
    给你一个字符串 s，找到 s 中最长的回文子串。

    Input: s = "babad"
    Output: "bab"

"""

"""
    动态规划，dp数组的含义比较好想，dp[i][j]代表，s[i:j]是否为回文串，这道题难就难在细节的处理。
    定义并初始化dp数组这个简单，我们需要想明白的是，这里面的状态是如何转移的，他并不是顺序的，甚至
    不是任何常规的顺序，一个回文串最大的特点是什么？首部和尾部永远相同，删掉一个首字母和一个尾字母，
    依旧还是回文串：dbabd => bab，那么这就是这里的状态转移方程，dp[i][j] = dp[i+1][j-1]，在
    辛辛苦苦知道如何转移了以后，如何遍历呢，画出n*n的图以后，可以发现，对角线上的，代表单个字符，全
    都是回文串，而对角线下方的，由于j>i，全都是不存在的，而根据状态转移方程，我们当前的dp[i][j]是由
    左下角的dp判定，然后沿着斜着向上的方向一次得出结果，借助leetcode官方非常新颖的思路，我们可以按照
    字符串的长度来由小到大遍历（外循环），j= L-i+1。然后要注意也是最难想到的细节是：1.当j大于n-1，我们
    要跳出循环；2.状态转移不单纯是dp[i][j] = dp[i+1][j-1]，如果回文串的长度为2，那么各自删掉一个，并
    不构成回文串，所以当长度大于等于3，我们按照状态转移方程，如果只是2，且两个字符相同，那么这也是一个回文串，
    且不依赖于“”空字符串，我们要额外给它们的dp赋值为True.

"""



class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        max_length = 1
        begin = 0
        if n <= 1:
            return s
        dp = [[False] * n for __ in range(n)]
        for i in range(n):
            dp[i][i] = True
        if s[0] == s[1]:
            dp[0][1] = True
            max_length += 1
        for L in range(2, n + 1):
            for i in range(n):
                j = L + i - 1
                if j > n - 1:
                    break
                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                if dp[i][j] and j - i + 1 > max_length:
                    begin = i
                    max_length = j - i + 1
        res = s[begin:begin + max_length]
        return res

