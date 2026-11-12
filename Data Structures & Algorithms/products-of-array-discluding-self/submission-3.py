class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = postfix = 1
        result = [0] * len(nums)

        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        
        for i in range(len(nums)-1,-1,-1):
            result[i] *= postfix
            postfix *= nums[i]
        
        return result