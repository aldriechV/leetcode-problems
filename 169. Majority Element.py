"""
169. Majority Element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Initial Approach:
1. Create a hash map to count occurrences of each element.
2. Iterate through the hash map to find the element with count greater than n/2.

Optimized Approach:
1. Keep a count and a target variable
2. Since the value of the highest occuring element is more than half the array length,
the highest occuring element will remain at the end if we increment count for the target
3. Increment count for each duplicates and decrement for non-duplicates.
4. return the final target value.


"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        target = 0
        for i in nums:
            if count == 0:
                target = i
            if i == target:
                count += 1
            else:
                count -= 1
        return target