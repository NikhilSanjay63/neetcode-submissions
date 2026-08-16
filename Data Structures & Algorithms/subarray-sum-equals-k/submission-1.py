class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        current_sum = 0
        prefix = {0:1}

        for i in nums:
            current_sum += i
            if (current_sum - k) in prefix:
                count += prefix[current_sum-k]
            
            if current_sum in prefix:
                prefix[current_sum] += 1
            else:
                prefix[current_sum] = 1
        
        return count