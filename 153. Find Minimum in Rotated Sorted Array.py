"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

- [4,5,6,7,0,1,2] if it was rotated 4 times.
- [0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

Initial Solution:
1. Set up pointers necessary for binary search.
2. Our challenge is not to find a number in the rotated array, but rather to find the minimum of the array. 
3. We would want to binary search as normal, however we want to figure out where exactly our minimum is. 
This would mean we need to find a way to move our low pointer to a minimum.
4. Set the pointers so that when the medium is compared to the right pointer, we can determine where our minimum is
    - If our medium is less than our high/right point, our minimum is closer to our medium, so we can set our lower pointer towards that medium
    - If our medium is more than our high/right point, our minimum is closer to our right point, so we can move our higher pointer towards the medium. 

"""

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 0
        high = len(nums) - 1

        while low < high:
            med = (low + high) // 2
            if nums[med] < nums[high]:
                high = med
            else:
                low = med + 1

        return nums[low]
