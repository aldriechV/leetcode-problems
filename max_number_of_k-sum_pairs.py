class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        - low pointer = first instance of k-x
        - high pointer = len -1 
        .pop() removes last element on list and .pop(#) removes first element 
        """
        ops = 0
        high = len(nums)-1
        low = 0
        nums.sort()
        while low < high:
            if nums[low] + nums[high] > k:
                high -= 1
            elif nums[low] + nums[high] < k:
                low += 1
            else:
                ops += 1
                nums[low] = nums[high] = 0
                low += 1
                high -= 1
        return ops