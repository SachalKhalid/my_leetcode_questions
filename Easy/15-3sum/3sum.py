class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]: continue
            j = i+1
            k = len(nums) - 1
            
            while j<k:
                totalSum =  nums[i] + nums[j] + nums[k]
                
                if totalSum < 0:
                    j = j + 1
                elif totalSum > 0:
                    k = k - 1
                else:
                    tem = [nums[i], nums[j],nums[k]]
                    ans.append(tem)
                    
                    while j<k and nums[j] == nums[j+1]: j = j + 1
                    while j<k and nums[k] == nums[k-1]: k = k - 1 
                    j = j + 1
                    k = k - 1
                    
            while i+1 < len(nums) and nums[i] == nums[i+1]: i = i + 1
        return ans