class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        array = [-1] * (len(nums)+1)
        for val in nums:
            array[val] = val
        
        for val in range(len(array)):
            if array[val] == -1:
                return val
        return 0