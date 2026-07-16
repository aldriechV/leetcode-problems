from math import gcd

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        
        """
        :type nums: List[int]
        :rtype: int
        """
        prefixGcd = []
        mx = 0
        total = 0
        
        for i in range(len(nums)):
            mx = max(nums[i], mx)
            prefixGcd.append(gcd(nums[i],mx))
        prefixGcd.sort()

        low = 0
        high = len(nums)-1
        while low < high:
            total += gcd(prefixGcd[low], prefixGcd[high])
            low += 1
            high -= 1
        
        return total
        

        


