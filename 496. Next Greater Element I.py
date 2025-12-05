"""

496. Next Greater Element I


The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.



"""


class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        diction = {}
        stack = [] # should be tracking nums2 

        for j in range(len(nums2)-1, -1, -1):
            while stack and nums2[j] >= nums2[stack[-1]]:
                print(stack)
                stack.pop()
                
            if stack:
                diction[nums2[j]] = nums2[stack[-1]]
            else:
                diction[nums2[j]] = -1
                
            stack.append(j)

        #answer setup, we can actually use a dictionary to keep track of the answers 
        ans = [0] * len(nums1)
        for i in range(len(nums1)):
            ans[i] = diction[nums1[i]]


        return ans