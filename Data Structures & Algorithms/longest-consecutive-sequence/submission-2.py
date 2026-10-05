class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxlen = 0
        numset = set(nums)

        for i in numset:
            if (i-1) not in numset:
                length = 0
                while (i+length) in numset:
                    length += 1
                maxlen = max(maxlen,length)
        
        return maxlen