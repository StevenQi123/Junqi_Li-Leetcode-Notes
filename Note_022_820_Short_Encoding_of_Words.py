"""
    来源：力扣（LeetCode）
    链接：https://leetcode.cn/problems/short-encoding-of-words
    难度：中等
    解法：翻转 + 排序 （本质上说这是字典树题，但是可以用可简便的方法）
    题目描述：
    单词数组words的有效编码由任意助记字符串s和下标数组indices 组成，且满足：words.length == indices.length
    助记字符串s以 '#' 字符结尾，对于每个下标 indices[i] ，s 的一个从 indices[i] 开始、到下一个 '#' 字符结束（但
    不包括 '#'）的子字符串恰好与 words[i]相等。给你一个单词数组words，返回成功对words进行编码的最小助记字符串s的长度 。

    Input_1: words = ["time", "me", "bell"]
    Output_1: 10
    Input_2: words = ["t"]
    Output_2: 2

"""

"""
    这道题的题目意思十分的晦涩难懂，那个indices数组完全没有用，不知道是干嘛的，恶心人，结合给的输入输出可以发现，
    好像每一个单词后面都要编码一个‘#’，只有当一个单词是另一个单词后缀时，可以少一个‘#’,那么这道题的本质，其实是
    找到所有可以作为后缀的单词，python有一个方法，str.startswith(str)可以用来判断前缀，那么我们将所有单词逆序，
    然后再借助排序，将开头一样的单词放在一个片段里。
"""

# Leetcode版
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        n = len(words)
        my_words = []
        res = 0
        for i in range(n):
            my_words.append(words[i][::-1])
        my_words.sort()
        for i in range(n-1):
            if my_words[i+1].startswith(my_words[i]):
                continue
            else:
                res += len(my_words[i]) + 1
        res += len(my_words[n-1]) + 1
        return res