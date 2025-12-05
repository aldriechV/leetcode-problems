"""
3432. Count Partitions with Even Sum Difference

You are given an integer array nums of length n.

A partition is defined as an index i where 0 <= i < n - 1, splitting the array into two non-empty subarrays such that:

Left subarray contains indices [0, i].
Right subarray contains indices [i + 1, n - 1].
Return the number of partitions where the difference between the sum of the left and right subarrays is even.

"""

class Solution(object):
    def countPartitions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        eSum = 0
        total = sum(nums)
        placeholder = 0

        for i in range(len(nums)-1):
            placeholder += nums[i]
            total -= nums[i]
            if (placeholder - total) % 2 == 0:
                eSum += 1
        return eSum

