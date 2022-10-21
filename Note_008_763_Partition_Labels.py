"""
    来源：力扣（LeetCode）
    链接：https://leetcode.cn/problems/partition-labels
    难度：中等
    解法：贪心 + 字典
    题目描述：
    字符串S由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。
    返回一个表示每个字符串片段的长度的列表。

    Input_1: S = "ababcbacadefegdehijhklij"
    Output_1: [9,7,8]
"""


# Leetcode版
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic = {x: index for index, x in enumerate(s)}
        result = []
        end = dic[s[0]]  # end = 'a':8
        num = 0
        for i in range(len(s)):
            num += 1
            if dic[s[i]] > end:
                end = dic[s[i]]
            if end == i:
                result.append(num)
                end = dic[s[i]] + 1
                num = 0
        return result


# ACM版
while True:
    try:
        s = input()
        dic = {x: index for index, x in enumerate(s)}
        result = []
        end = dic[s[0]]  # end = 'a':8
        num = 0
        for i in range(len(s)):
            num += 1
            if dic[s[i]] > end:
                end = dic[s[i]]
            if end == i:
                result.append(num)
                end = dic[s[i]] + 1
                num = 0
        print(result)


    except:
        break
