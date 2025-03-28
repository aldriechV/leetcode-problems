class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        found = set()
        duplicates = []
 
        for num in nums:
            if num in found:
                duplicates.append(num)
            else:
                found.add(num)
 
        return duplicates
