"""
1437. Check If All 1's Are at Least Length K Places Away

Given a binary array nums and an integer k, return true if all 1's are at least k places away from each other, otherwise return false.

"""

class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        gap = 0
        change = False
        for i in nums:
            if i == 1:
                if gap <= k and change:
                    return False
                change = True
                gap = 0 
            gap += 1
        return True