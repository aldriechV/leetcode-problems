"""
41. First Missing Positive

Given an unsorted integer array nums, return the smallest missing positive integer.

1. Initial Solution:
- Create a hash map (dictionary) to track the presence of each positive integer in the array
- Iterate through the array and populate the hash map with the integers as keys.
- Initialize a variable smallest to 1, which represents the smallest positive integer we are looking for.
- Use a while loop to check if smallest is present in the hash map.
- If it is present, increment smallest by 1 and continue checking.
- Once we find a smallest that is not present in the hash map, return that value.
- Runtime Complexity: O(n) since we traverse the array once to build the hash map and then potentially traverse up to n to find the missing positive.
- Space Complexity: O(n) due to the additional space used by the hash map.
"""


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tracker = {}
        for i in nums:
            if i in tracker:
                tracker[i] += 1
            else:
                tracker[i] = 1
        smallest = 1
        while smallest in tracker:
            smallest += 1
        return smallest