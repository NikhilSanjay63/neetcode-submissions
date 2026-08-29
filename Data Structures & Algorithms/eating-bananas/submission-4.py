class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def k_works(k):
            hours = 0
            for p in piles:
                hours += math.ceil(p/k)
            
            return hours <= h
        
        left,right = 1,max(piles)

        while left < right:
            middle = (left+right)//2
            if k_works(middle):
                right = middle
            else:
                left = middle + 1
        
        return left