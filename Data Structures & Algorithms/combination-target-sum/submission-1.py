class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(start_index,path,current_sum):
            if current_sum == target:
                result.append(path[:])
                return
            if current_sum > target:
                return
            
            for i in range(start_index,len(nums)):
                path.append(nums[i])
                dfs(i,path,current_sum + nums[i])
                path.pop()
        
        dfs(0,[],0)
        return result