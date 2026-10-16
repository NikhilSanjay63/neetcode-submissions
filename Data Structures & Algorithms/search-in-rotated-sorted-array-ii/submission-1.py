class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left,right = 0, len(nums) -1

        while left <= right:
            middle = (left+right)//2

            if nums[middle] == target:
                return True
            
            elif nums[left] == nums[middle] == nums[right]:
                left += 1
                right -= 1
            
            elif nums[middle] > nums[right]:
                if nums[left] <= target < nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
            
            else:
                if nums[middle] < target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1
        
        return False