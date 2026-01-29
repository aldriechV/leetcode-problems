"""
Docstring for 75. Sort Colors

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

"""


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        counts = {0: 0, 1: 0, 2: 0}
        for n in nums:
            counts[n] += 1
            index = 0
            
        for value in (0, 1, 2):
            for _ in range(counts[value]):
                nums[index] = value
                index += 1