"""
    来源：力扣（LeetCode）
    链接：https://leetcode.cn/problems/candy
    难度：困难
    解法：两次遍历的贪心
    题目描述：
    n个孩子站成一排。给你一个整数数组ratings表示每个孩子的评分。你需要按照以下要求，给这些孩子分发糖果：每个孩子至少
    分配到1个糖果。相邻两个孩子评分更高的孩子会获得更多的糖果。请你给每个孩子分发糖果，计算并返回需要准备的 最少糖果数目 。

    Input_1: ratings = [1,0,2]
    Output_1: 5 # 2,1,2
    Input_2: ratings = [1,2,2]
    Output_2：4 # 1,2,1

"""

"""
    左扫+右扫，从左往右遍历时，当右边比左边大，ratings[i+1] > ratings[i]，更新右边的糖果数，确保每一个孩子与他右边的
    孩子的糖果数满足题目要求，从右往左扫时，当左边比右边大，ratings[i-1] > ratings[i]，更新左边的糖果数，确保每一个孩子
    与他左边的孩子糖果数满足题目要求。如果用一次遍历，同时既考虑左边也考虑右边，那就会顾此失彼，达不到全局最优。
"""

# Leetcode版
class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1 for i in range(len(ratings))]

        for i in range(len(ratings) - 1):
            if ratings[i + 1] > ratings[i]:
                candies[i + 1] = candies[i] + 1
        for i in range(len(ratings) - 1, 0, -1):
            if (ratings[i - 1] > ratings[i]) & (candies[i - 1] <= candies[i]):
                candies[i - 1] = candies[i] + 1

        return sum(candies)

# ACM版

while True:
    try:
        ratings = list(map(int,input().split()))
        candies = [1 for i in range(len(ratings))]
        for i in range(len(ratings) - 1):
            if ratings[i + 1] > ratings[i]:
                candies[i + 1] = candies[i] + 1
        for i in range(len(ratings) - 1, 0, -1):
            if (ratings[i - 1] > ratings[i]) & (candies[i - 1] <= candies[i]):
                candies[i - 1] = candies[i] + 1
        print(sum(candies))

    except:
        break