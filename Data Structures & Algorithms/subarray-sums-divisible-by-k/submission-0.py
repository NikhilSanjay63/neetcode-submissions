class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        current_sum = 0
        reminders = {0:1}

        for i in nums:
            current_sum += i
            rem = current_sum % k

            if rem in reminders:
                count += reminders[rem]
                reminders[rem] += 1
            else:
                reminders[rem] = 1
        
        return count