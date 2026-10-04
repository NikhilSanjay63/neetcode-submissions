class Solution:
    def minWindow(self, s: str, t: str) -> str:
        result = [-1,-1]
        resultlen = float('inf')

        countT, window = {}, {}

        for i in range(len(t)):
            countT[t[i]] = countT.get(t[i],0) + 1
        
        have, need = 0, len(countT)
        l = 0

        for r in range(len(s)):
            ch = s[r]
            window[ch] = window.get(ch,0) + 1

            if ch in countT and window[ch] == countT[ch]:
                have += 1
            
            while have == need:
                if (r-l+1) < resultlen:
                    result = [l,r]
                    resultlen = (r-l+1)
                
                window[s[l]] -= 1

                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                
                l += 1
        
        l,r = result
        return s[l:r+1] if resultlen != float('inf') else ""
