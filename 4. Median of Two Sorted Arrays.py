"""
4. Median of Two Sorted Arrays

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.\
The overall run time complexity should be O(log (m+n)).

"""


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums3 = []
        i = 0
        j = 0
        n = len(nums1)
        m = len(nums2)
        while i < n and j < m:
            if nums1[i] <= nums2[j]:
                nums3.append(nums1[i])
                i += 1
            else:
                nums3.append(nums2[j])
                j += 1

        # copy remaining elements from arr1
        while i < n:
            nums3.append(nums1[i])
            i += 1

        # copy remaining elements from arr2
        while j < m:
            nums3.append(nums2[j])
            j += 1

        print(nums3)
        #binary search!
        a = len(nums3)
        return nums3[a // 2] if a % 2 == 1 else (nums3[a // 2] + nums3[(a // 2) - 1]) / 2.0