"""
229. Majority Element II

Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Initial Approach:
1. Create a hash map to count occurrences of each element.
2. Iterate through the hash map to find the element with count greater than n/2.

Optimized Approach:
1. Keep a count and a target variable
2. Since the value of the highest occuring element is more than a third of the array length,
the highest occuring element will remain at the end if we increment count for the target
3. Increment count for each duplicates and decrement for non-duplicates.
4. return the final target value.
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