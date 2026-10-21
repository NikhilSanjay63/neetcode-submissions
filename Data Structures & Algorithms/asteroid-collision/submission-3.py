class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                if stack[-1] > -a:
                    break
                if stack[-1] == -a:
                    stack.pop()
                    break
                else:
                    stack.pop()
            else:
                stack.append(a)
        
        return stack
