"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates, return the number of unique elements k.

The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.


1. Initial Solution:
- Create a hash map (dictionary) to track the presence of each integer in the array.
- Iterate through the array and populate the hash map with the integers as keys.
- Extract the keys from the hash map and sort them to get the unique elements in order.
- Overwrite the first k elements of the original array with these unique sorted elements.
"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        table = {}
        for i in nums:
            if i in table:
                table[i] += 1
            else:
                table[i] = 1
        non_dupes = sorted(table.keys())
        for i in range(len(non_dupes)):
            nums[i] = non_dupes[i]
        
        return len(non_dupes)