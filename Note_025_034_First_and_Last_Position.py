"""
    来源：力扣（LeetCode）
    链接：https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array
    难度：中等
    解法：字典/二分查找
    题目描述：
    给你一个按照非递减顺序排列的整数数组nums，和一个目标值target。请你找出给定目标值在数组中的开始位置和结束位置。
    如果数组中不存在目标值 target，返回[-1, -1]。你必须设计并实现时间复杂度为O(log n)的算法解决此问题。

    Input_1: nums = [5,7,7,8,8,10], target = 8
    Output_1: [3,4]
    Input_2: nums = [5,7,7,8,8,10], target = 6
    Output_2: [-1,-1]

"""

# 字典版
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        dic1 = {x:index for index,x in enumerate(nums)}
        if target not in dic1:
            return [-1,-1]
        else:
            right = dic1[target]
            nums.reverse()
            dic2 = {x:index for index,x in enumerate(nums)}
            left = len(nums)-dic2[target]-1
            return [left,right]

# 二分查找版
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def my_search(nums, target, k):
            left = 0
            right = len(nums) - 1
            mid = 0
            ans = right + 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > target or (k and nums[mid] >= target):
                    right = mid - 1
                    ans = mid
                else:
                    left = mid + 1
            return ans

        left = my_search(nums, target, True)
        right = my_search(nums, target, False) - 1
        if left <= right <= len(nums) - 1 and nums[left] == target and nums[right] == target:
            return [left, right]
        else:
            return [-1, -1]


