"""
Docstring for 1984. Minimum Difference Between Highest and Lowest of K Scores


You are given a 0-indexed integer array nums, where nums[i] represents the score of the ith student. You are also given an integer k.

Pick the scores of any k students from the array so that the difference between the highest and the lowest of the k scores is minimized.

Return the minimum possible difference.

 
"""




class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        yes = nums.sort()
        answer = nums[k - 1] - nums[0]
        for i in range(0, len(nums) - k + 1):
            answer = min(answer, nums[i + k - 1] - nums[i])
        return answer