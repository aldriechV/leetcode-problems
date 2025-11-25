"""
2455. Average Value of Even Numbers That Are Divisible by Three

Given an integer array nums of positive integers, return the average value of all even integers that are divisible by 3.

Note that the average of n elements is the sum of the n elements divided by n and rounded down to the nearest integer.
"""

class Solution(object):
    def averageValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        avg = 0
        total = 0
        for i in nums:
            if i % 3 == 0 and i % 2 == 0:
                total += i
                avg += 1
        
        return total if avg == 0 else total / avg
                 
        