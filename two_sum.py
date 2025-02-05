class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in map:
                return [map[diff], i]
            map[n] = i
        return -1


"""
Time and Space Complexity:
Time: O(N) traveling through array of len(n) with constant speeed for map traversal
Space: O(N) only grows as big as the map gets
"""