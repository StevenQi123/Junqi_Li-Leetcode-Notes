"""
    来源：力扣（LeetCode）
    链接：https://leetcode.cn/problems/search-in-rotated-sorted-array
    难度：中等
    解法：二分查找
    题目描述：
    整数数组nums按升序排列，数组中的值互不相同 。在传递给函数之前，nums在预先未知的某个下标 k（0 <= k < nums.length）
    上进行了 旋转，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标
    从 0开始计数）。例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为[4,5,6,7,0,1,2] 。给你旋转后的数组nums和一个
    整数 target，如果 nums中存在这个目标值 target ，则返回它的下标，否则返回-1。
    你必须设计一个时间复杂度为 O(log n)的算法解决此问题。

    Input_1: nums = [4,5,6,7,0,1,2], target = 0
    Output_1: 4
    Input_2: nums = [4,5,6,7,0,1,2], target = 3
    Output_2: -1

"""

"""
    依然还是二分查找，但是经过旋转，不再是非递减序列，它是一个两段非递减序列拼接而成的序列，我们要利用好
    它们各自递增的性质，想想二分查找为什么用于非递减序列，因为递增，我们可以通过nums[mid]来判断，下一步
    在左侧还是右侧继续查找，这里其实也是一样的，无论mid落在哪里，左右两侧总至少有一侧是非递减序列，依然也能
    用来判断，只不过要多一步判断，左侧还是右侧是非递减序列，这个其实也非常简单，只需要用nums[mid]和nums[0]
    进行比较。
"""

# Leetcode版
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        n = right
        mid = 0
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            # 左段有序
            if nums[mid] >= nums[0]:
                if nums[0] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target <= nums[n]:
                    left = mid + 1
                else:
                    right = mid -1
        return -1

