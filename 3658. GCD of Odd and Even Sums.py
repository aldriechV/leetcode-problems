from math import gcd

class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        oddNum = 0
        evenNum = 0
        evenCalc = 2
        oddCalc = 1
        for i in range(n):
            oddNum += oddCalc
            evenNum += evenCalc
            oddCalc += 2
            evenCalc += 2

        return gcd(oddNum, evenNum)

