"""
41. First Missing Positive

Given an unsorted integer array nums, return the smallest missing positive integer.

"""


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tracker = {}
        for i in nums:
            if i in tracker:
                tracker[i] += 1
            else:
                tracker[i] = 1
        smallest = 1
        while smallest in tracker:
            smallest += 1
        return smallest