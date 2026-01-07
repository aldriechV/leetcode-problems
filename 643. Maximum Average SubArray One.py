"""

643. Maximum Average Subarray I


You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

"""



class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int=
        :rtype: float
        """
        window_sum = sum(nums[:k])
        maxSum = window_sum
        
        for i in range(k, len(nums)):
            #The actual sliding window part
            window_sum += nums[i] - nums[i - k]
            maxSum = max(window_sum, maxSum)

        return maxSum / float