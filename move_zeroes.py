class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        - two pointer problem
        - move the left pointer only when it is non zero 
        - constantly move right pointer 
        """
        counter = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[counter], nums[i] = nums[i], nums[counter]
                counter += 1