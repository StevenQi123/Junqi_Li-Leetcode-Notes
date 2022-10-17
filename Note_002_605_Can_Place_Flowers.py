"""
    来源：力扣（LeetCode）
    链接：https://leetcode.cn/problems/can-place-flowers
    难度：简单
    解法：贪心算法
    题目描述：
    假设有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花不能种植在相邻的地块上，它们会争夺水源，两者都会死去。
    你一个整数数组flowerbed表示花坛，由若干 0 和 1 组成，其中 0 表示没种植花，1 表示种植了花。另有一个数 n，
    能否在不打破种植规则的情况下种入n朵花？能则返回 true ，不能则返回 false。

    Input_1：flowerbed = [1,0,0,0,1], n = 1
    Output_1：true
    Input_2：flowerbed = [1,0,0,0,1], n = 2
    Output_2：false

"""

# Leetcode版v1
"""
    第一版的做题时，不会处理边界，傻瓜式的将长度为1和为2单独拿出来写，对于长度大于等于3的，判断前后是否没有种花，
    如果都没有，则可以种并且修改当前的值，每次只考虑当前一格行不行
"""


class Solution_1:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flower = 0
        end = len(flowerbed) - 1
        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                flowerbed[0] = 1
                flower += 1
        elif len(flowerbed) == 2:
            if (flowerbed[0]) == 0 & (flowerbed[1] == 0):
                flowerbed[0] = 1
                flower += 1
        else:
            if (flowerbed[0] == 0) & (flowerbed[1] == 0):
                flowerbed[0] = 1
                flower += 1
            for i in range(1, end):
                if (flowerbed[i - 1] == 0) & (flowerbed[i + 1] == 0) & (flowerbed[i] == 0):
                    flowerbed[i] = 1
                    flower += 1
            if (flowerbed[end - 1] == 0) & (flowerbed[end] == 0):
                flowerbed[end] = 1
                flower += 1
        if flower >= n:
            return True
        else:
            return False


# Leetcode版v2
"""
    将列表加一个头加一个尾，保证长度总是大于等于3，方便把所有情况写在一起
"""


class Solution_2:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        new_flowerbed = [0] + flowerbed + [0]
        flower = 0
        len_bed = len(new_flowerbed)
        if len_bed < 3:
            return False
        for i in range(1, len_bed - 1):
            if (new_flowerbed[i - 1] == 0) & (new_flowerbed[i + 1] == 0) & (new_flowerbed[i] == 0):
                new_flowerbed[i] = 1
                flower += 1
        if flower >= n:
            return True
        else:
            return False


# ACM版
"""
    输出1代表True，输出0代表False
"""
while True:
    try:
        # 输入部分
        flowerbed = list(map(int, input().split()))
        n = int(input())
        new_flowerbed = [0] + flowerbed + [0]
        flower = 0
        len_bed = len(new_flowerbed)
        if len_bed < 3:
            print(0)
            break
        for i in range(1, len_bed - 1):
            if (new_flowerbed[i - 1] == 0) & (new_flowerbed[i + 1] == 0) & (new_flowerbed[i] == 0):
                new_flowerbed[i] = 1
                flower += 1
        if flower >= n:
            print(1)
            break
        else:
            print(0)
            break
    except:
        break
