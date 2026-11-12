class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = []

        for key,value in counter.items():
            if len(heap) < k:
                heapq.heappush(heap,(value,key))
            else:
                heapq.heappushpop(heap,(value,key))
        
        return [heap[i][1] for i in range(len(heap))]