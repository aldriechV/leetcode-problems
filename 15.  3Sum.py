"""
15. 3Sum
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        1. Define the rules in code first, then work on a solution
        2. i j and k cannot equal each other, and i j k need to equal 0
        3. No duplicate triples
        

        - for loop to iterate i
        - while loop to check j and k, surely there is a more efficient way to move the pointers up and down
        """
        nums.sort() # needed for two pointer solution
        n = len(nums)
        sol = []

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            j, k = i + 1, n - 1        
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == 0:
                    sol.append([nums[i], nums[j], nums[k]])
                    k -= 1
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                elif s < 0:
                    j += 1
                else:
                    k -= 1
        return sol

