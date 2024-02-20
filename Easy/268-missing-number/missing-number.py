class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        array = [-1] * (len(nums)+1)
        for val in nums:
            array[val] = val
        
        for val in array:
            if val == -1:
                return array.index(val)