"""
    来源：力扣（LeetCode）
    链接：https://leetcode.cn/problems/valid-parentheses
    难度：简单
    解法：栈
    题目描述：
    给定一个只包括 '('，')'，'{'，'}'，'['，']'的字符串s，判断字符串是否有效。有效字符串需满足：
    左括号必须用相同类型的右括号闭合。
    左括号必须以正确的顺序闭合。
    每个右括号都有一个对应的相同类型的左括号。

    Input_1: s = "()[]{}"
    Output_1：true
    Input_2: s = "(]"
    Output_2: false

"""

class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        if n % 2 == 1:
            return False
        pairs = {')':'(', '}':'{', ']':'['}
        res = []
        for ch in s:
            if ch not in pairs:
                res.append(ch)
            else:
                if not res or res[-1] != pairs[ch]:
                    return False
                else:
                    res.pop()
        return len(res) == 0
