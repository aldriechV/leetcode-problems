class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def findFirst():
            low = 0
            high = len(nums)-1
            ans = -1
            
            while low <= high:
                med = (low + high) // 2
                if nums[med] == target: 
                    ans = med
                    high = med -1
                elif nums[med] < target:
                    low = med + 1
                else:
                    high = med -1

            return ans

        def findSec():
            low = 0
            high = len(nums)-1
            ans = -1
            
            while low <= high:
                med = (low + high) // 2
                if nums[med] == target: 
                    ans = med
                    low = med + 1
                elif nums[med] < target:
                    low = med + 1
                else:
                    high = med -1

            return ans

        return [findFirst(), findSec()]