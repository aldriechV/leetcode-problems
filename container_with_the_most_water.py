class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        - two pointers starting from each end
        - find the largest possible area (max(res, area))
        - move pointers based on height, stop once the whole array is traversed
        """
        low = 0
        high = len(height) - 1
        res = 0
        for i in range(len(height)):
            area = (high - low) * min(height[low], height[high])
            res = max(res, area)
            if height[low] > height[high]:
                high -= 1
            else:
                low += 1
        
        return res

        