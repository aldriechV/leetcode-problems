"""
# 283. Move Zeroes

## **Problem Statement**  
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

## **Approach**  
### **2. Optimized Approach**  
- Employs a two pointer solution, setting both the left and right pointer at the start of the 
- Increment the right pointer using the index of the for loop
- The left pointer will stay behind and increment only if the right pointer catches an index that is not a 0
- Time Complexity: O(n) (one pass through `nums`)  
- Space Complexity: O(1) (No additional data structures or space needs to be made)

## Final Implementation Provided Below:  
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        counter = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[counter], nums[i] = nums[i], nums[counter]
                counter += 1
