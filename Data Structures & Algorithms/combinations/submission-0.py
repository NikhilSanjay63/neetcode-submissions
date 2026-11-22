class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        comb = []

        def backtrack(start):
            if len(comb) == k:
                result.append(comb.copy())
                return
            
            need = k - len(comb)
            max_need = n - need + 1
            for num in range(start,max_need + 1):
                comb.append(num)
                backtrack(num + 1)
                comb.pop()
        
        backtrack(1)
        return result