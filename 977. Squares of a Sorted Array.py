class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        moves = []
        for i in range(len(nums)):
            moves.append(nums[i] * nums[i])
        moves.sort()

        return moves

# Solution can also be implemented using two pointers, two pointers is faster due to an O(n) runtime

class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=0
        r=len(nums)-1
        pos=r

        res=[0]*len(nums)

        while l<=r:
            lq=nums[l]*nums[l]
            rq=nums[r]*nums[r]
            if lq>rq:
                res[pos]=lq
                l+=1
            else:
                res[pos]=rq
                r-=1
            pos-=1
        return res

        
