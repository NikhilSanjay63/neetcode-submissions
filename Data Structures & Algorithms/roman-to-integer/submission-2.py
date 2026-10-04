class Solution:
    def romanToInt(self, s: str) -> int:
        numbers = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        total = 0

        for i in range(len(s)):
            if i < len(s) - 1 and numbers[s[i]] < numbers[s[i+1]]:
                total -= numbers[s[i]]
            else:
                total += numbers[s[i]]
        
        return total