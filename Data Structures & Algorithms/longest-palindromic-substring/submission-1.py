class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ''
        resultlen = float('-inf')

        for i in range(len(s)):
            #odd
            left,right = i,i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right-left+1) > resultlen:
                    result = s[left:right+1]
                    resultlen = (right-left+1)
                left -= 1
                right += 1
            
            #even
            left,right = i,i+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right-left+1) > resultlen:
                    result = s[left:right+1]
                    resultlen = (right-left+1)
                left -= 1
                right += 1
        
        return result