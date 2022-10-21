"""
    来源：力扣（LeetCode）
    链接：https://leetcode.cn/problems/jump-game
    难度：中等
    解法：贪心算法
    题目描述：
    给定一个非负整数数组nums，你最初位于数组的第一个下标 。数组中的每个元素代表你在该位置可以跳跃的最大长度。
    判断你是否能够到达最后一个下标。

    Input_1: nums = [2,3,1,1,4]
    Output_1: true
    Input_2: nums = [3,2,1,0,4]
    Output_2: false
"""

"""
    这道题最关键的一个点在于，凡是能够跳到的点的所有左边的点都是可以跳到的，我们把可以看作是起跳点的，跳一次能到达的最远距离
    和数组的长度-1做比较，而是否能够当作起跳点，就看在遍历时，当前能跳的最远距离，是否大于等于该点索引
"""

# Leetcode版
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if nums == []:
            return false
        dis = nums[0]
        for i in range(len(nums)):
            if dis >= i:
                dis = max(dis,i+nums[i])
        return dis >= len(nums)-1

# ACM版
while True:
    try:
        nums = list(map(int,input().split()))
        if nums == []:
            print(False)
        dis = nums[0]
        for i in range(len(nums)):
            if dis >= i:
                dis = max(dis, i + nums[i])
        print(dis >= len(nums) - 1)

    except:
        break