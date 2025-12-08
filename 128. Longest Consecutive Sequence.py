"""
128. Longest Consecutive Sequence

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
"""

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        1. first store all the numbers in a set
        2. then run a loop and check if a numbeer exists before it
        3. then check if the next number is in the list,if it is then increase the streak
        4. then use the max(function) to compare lengths of all series and return it
        """
        longest = 0
        checker = set(nums)

        for i in checker:
            if (i-1) not in checker:
                streak = 1
                start = i
            
                while start+1 in checker:
                    streak += 1
                    start += 1
                longest = max(longest, streak)

        return longest