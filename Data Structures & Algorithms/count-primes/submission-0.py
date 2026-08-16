class Solution:
    def countPrimes(self, n: int) -> int:
        seen = [False] * n
        ans = 0
        for num in range(2,n):
            if not seen[num]:
                ans += 1
                for i in range(num * num, n, num):
                    seen[i] = True
        return ans