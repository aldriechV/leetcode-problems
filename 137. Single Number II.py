"""
Docstring for 137. Single Number II

Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.

"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        table = {}
        for i in nums:
            if i in table:
                table[i] += 1
            else:
                table[i] = 1
        for i in table:
            if table[i] == 1:
                return i
        return -1