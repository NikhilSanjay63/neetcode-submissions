class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for index,value in enumerate(nums):
            hashmap[value] = index
        
        for i in range(len(nums)):
            com = target - nums[i]
            if com in hashmap and hashmap[com] != i:
                return [i,hashmap[com]]