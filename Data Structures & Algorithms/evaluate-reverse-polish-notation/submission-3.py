class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for ch in tokens:
            if ch == '+':
                stack.append(stack.pop() + stack.pop())
            elif ch == '-':
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
            elif ch == '*':
                stack.append(stack.pop() * stack.pop())
            elif ch == '/':
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(ch))
        
        return stack[0]