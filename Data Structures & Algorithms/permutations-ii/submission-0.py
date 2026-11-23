class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        perms = []
        count = Counter(nums)

        def backtrack():
            if len(perms) == len(nums):
                result.append(perms.copy())
                return
            
            for num in count:
                if count[num] > 0:
                    perms.append(num)
                    count[num] -= 1

                    backtrack()

                    count[num] += 1
                    perms.pop()
        
        backtrack()
        return result
