class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def kspeed(k):
            time = 0
            for p in piles:
                time += math.ceil(p/k)
            return time <= h
        
        left,right = 1,max(piles)
        while left < right:
            middle = (left+right)//2
            if kspeed(middle):
                right = middle
            else:
                left = middle + 1
        
        return left