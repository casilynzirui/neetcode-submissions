class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        currentCounter = 0
        maxCounter = 0
        
        for num in nums:
            if num == 1:
                currentCounter += 1
            if num == 0:
                maxCounter = max(maxCounter, currentCounter)
                currentCounter = 0
        
        maxCounter = max(maxCounter, currentCounter)
        return maxCounter