"""
33, Search in Rotated Sorted Array
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.




"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums) - 1
        med = 0
        while low < high:
            med = (low + high) // 2
            if nums[med] < nums[high]:
                high = med
            else:
                low = med + 1
        rot = low
        
        low = 0
        high = len(nums)-1
        while low <= high:
            pivot = (low + high) // 2
            trueMed = (rot + pivot) % len(nums)
            if nums[trueMed] == target:
                return trueMed
            elif nums[trueMed] < target:
                low = pivot + 1
            else:
                high = pivot - 1

        return -1

