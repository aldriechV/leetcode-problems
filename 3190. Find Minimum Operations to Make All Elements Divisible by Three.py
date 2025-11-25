"""
3190. Find Minimum Operations to Make All Elements Divisible by Three

You are given an integer array nums. In one operation, you can add or subtract 1 from any element of nums.

Return the minimum number of operations to make all elements of nums divisible by 3.
"""

class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ops = 0
        for i in nums:
            if i % 3 == 0:
                continue
            elif (i + 1) % 3 == 0 or (i - 1) % 3 == 0:
                ops += 1
            else:
                continue
        return ops 
    