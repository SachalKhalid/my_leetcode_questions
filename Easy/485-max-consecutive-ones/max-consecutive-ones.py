class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = 0
        maxcn = 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                cnt = 0
            else:
                cnt += 1
            
            maxcn = max(maxcn, cnt)
        return maxcn
        