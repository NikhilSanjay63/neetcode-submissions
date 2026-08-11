class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {'[':']','{':'}','(':')'}
        stack = []

        for ch in s:
            if ch in pairs:
                stack.append(pairs[ch])
            else:
                if not stack or stack.pop() != ch:
                    return False
        
        return not stack