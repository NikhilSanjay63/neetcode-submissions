class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = set()
        for i in nums:
            if i not in unique:
                unique.add(i)
            else:
                return True
        
        return False