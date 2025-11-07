"""

Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Solution implementation:
1. Create two arrays to store the maximum height to the left and right of each index. This is done to calculate the water that can be trapped at each index.
2. Iterate thru the minimum of the left and right max heights at each index, subtracting the height at that index to get the water trapped.
3. Sum up the water trapped at each index to get the total amount of trapped water.
"""

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        length = len(height)
        left = [0] * length
        right = [0] * length

        #create my array
        left[0] = height[0]
        for i in range(1, length):
            left[i] = max(left[i-1], height[i])

        right[length-1] = height[length - 1]
        for i in range(length-2, -1, -1):
            right[i] =  max(right[i+1], height[i])
        
        #find the water
        water = 0 
        for i in range(length):
            water += min(left[i], right[i]) - height[i]
        
        return water
    