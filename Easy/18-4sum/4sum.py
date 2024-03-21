class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]: continue
            for j in range(i+1, len(nums)):
                if j != (i+1) and nums[j] == nums[j-1]: continue
                k = j+1
                l = len(nums) - 1
                while k<l:
                    totalSum =  nums[i] + nums[j] + nums[k] + nums[l]
                    if totalSum == target:
                        tem = [nums[i], nums[j],nums[k], nums[l]]
                        ans.append(tem)
                        k += 1
                        l -= 1
                        while k<l and nums[k] == nums[k-1]: k += 1
                        while k<l and nums[l] == nums[l+1]: l -= 1 
                       
                    elif totalSum < target:
                        k = k + 1
                    else:
                        l = l - 1
                        
                # while j+1 < len(nums) and nums[j] == nums[j+1]: j = j + 1
            # while i+1 < len(nums) and nums[i] == nums[i+1]: i = i + 1
        return ans