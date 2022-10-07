"""
    来源：力扣（LeetCode）
    链接：https://leetcode.cn/problems/assign-cookies
    难度：简单
    题目描述：
    假设你是一位很棒的家长，想要给你的孩子们一些小饼干。但是，每个孩子最多只能给一块饼干。
    对每个孩子 i，都有一个胃口值g[i]，这是能让孩子们满足胃口的饼干的最小尺寸；并且每块饼干j，
    都有一个尺寸 s[j]。如果 s[j]>= g[i]，我们可以将这个饼干 j 分配给孩子 i ，这个孩子会得到满足。
    你的目标是尽可能满足越多数量的孩子，并输出这个最大数值。

    Input_1:g = [1,2,3], s = [1,1]
    Output_1: 1
    Input_2:g = [1,2], s = [1,2,3]
    Output_2: 2

"""

"""
    最经典的贪心算法题目，贪心算法，顾名思义，追求局部最优解，选择暂时不去考虑全局情况
    简单一点的做法是，先排序，每次满足一个小孩子，饥饿度越小的孩子越容易满足
"""


# Leetcode版
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # 若没有规定要将排序算法写出，可以直接使用.sort()
        g.sort()
        s.sort()
        # 类似于使用双指针移动
        child = 0
        cookie = 0
        # 跳出循环的条件
        while (cookie < len(s)) & (child < len(g)):
            if s[cookie] >= g[child]:
                child += 1
            cookie += 1

        return child


# ACM版
""" 
    一些基础的Python ACM模式输入输出知识，后续用到更复杂的会说明
    输入时分为两行，第一行g，第二行s，不需要括号，用空格隔开
    1 2 3
    1 1
    
    input()函数从标准输入中读取一个字符串string，以换行符为结束字符
    spilt()函数默认以空格为分隔字符，例split(',')以逗号为分隔符
    b = input().split()   b = ['1', '2', '3', '4', '5']
    c = [int(i) for i in b]   c = [1, 2, 3, 4, 5]
    or使用map()进行转换
    e = map(int, input().split())  此时e是一个map迭代器，不能赋值，也不能索引
    f = list(e)  e = [1, 2, 3, 4, 5]
    
    print(a, b, c)，print默认以空格为分隔符
    output：1 2 3
    print(a, b, c, sep=',')，以逗号为分隔符
    output：1,2,3
    
    res = [1, 2, 3]
    print(res) ouput: [1, 2, 3]
    for i in range(len(res)):
        print(res[i])
    output: 1
            2
            3
    for i in range(len(res)):
        print(res[i], end=' ')  end的默认值是'\n'，即换行
    output: 1 2 3
    
    res = ['a', 'b', 'c']
    print("".join(res))
    output: abc
    print("*".join(res))
    output: a*b*c

"""

while True:
    try:
        # 输入部分
        g = list(map(int, input().split()))  # g = [1,2,3]
        s = list(map(int, input().split()))  # s = [1,1]
        g.sort()
        s.sort()
        child = 0
        cookie = 0
        while (cookie < len(s)) & (child < len(g)):
            if s[cookie] >= g[child]:
                child += 1
            cookie += 1
        print(child)

    except:
        break
