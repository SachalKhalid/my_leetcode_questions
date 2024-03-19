class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sumVal = 0
        maxVal = float('-inf')
        for i in range(len(nums)):
            sumVal = nums[i] + sumVal
            if sumVal > maxVal:
                maxVal = sumVal
            
            if sumVal < 0:
                sumVal = 0
        return maxVal
                