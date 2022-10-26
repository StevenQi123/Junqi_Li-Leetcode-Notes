"""
    来源：力扣（LeetCode）
    链接：https://leetcode.cn/problems/house-robber-ii
    难度：中等
    解法：动态规划
    题目描述：
    你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都围成一圈，这意味着第
    一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，
    系统会自动报警。给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，今晚能够偷窃到的最高金额。

    Input_1: nums = [2,3,2]
    Output_1: 3
    Input_1: nums = [1,2,3,1]
    Output_1: 4

"""

"""
    动态规划的解体关键还是在于找到状态转移方程，要坚信。这类题目都是有状态转移方程的，只不过为了找到全局最优，
    我们需要往前看1个或者2个状态，而不是简单的看前一个，然后就觉得只是局部最优，考虑不到全局，动态规划的本质是
    暴力枚举，但是在每一次枚举前，我们或多或少可以利用以往的状态，尽管不是上一个状态。对于环形街道，有一个很不错
    的思想，既然第一个和最后一个无法同时选取，那么就构造出两个街道，一个不能偷最后一个，一个不能偷第一个，最后取
    两者最大值。

"""


# Leetcode版
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        def my_rob(nums):
            prev, cur = 0, 0
            for num in nums:
                tmp = cur
                cur = max(cur, prev + num)
                prev = tmp
            return cur

        res = max(my_rob(nums[1:]), my_rob(nums[:n - 1]))
        return res


# ACM版
def my_rob(nums):
    prev, cur = 0, 0
    for num in nums:
        tmp = cur
        cur = max(cur, prev + num)
        prev = tmp
    return cur


while True:
    try:
        nums = list(map(int, input().split()))
        n = len(nums)
        if n == 1:
            print(nums[0])
        else:
            res = max(my_rob(nums[1:]), my_rob(nums[:n - 1]))
            print(res)

    except:
        break
