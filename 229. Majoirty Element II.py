"""
229. Majority Element II

Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        threshold = (len(nums) // 3) + 1

        ans = []
        total = {}
        for i in nums:
            if i in total:
                total[i] += 1
            else:
                total[i] = 1
        
        for i in total:
            if total[i] >= threshold:
                ans.append(i)
        return ans