class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == '+':
                b, a = stack.pop(), stack.pop()
                stack.append(int(a) + int(b))
            elif t == '-':
                b, a = stack.pop(), stack.pop()
                stack.append(int(a) - int(b))
            elif t == '/':
                b, a = stack.pop(), stack.pop()
                stack.append(int(int(a) / int(b)))
            elif t == '*':
                b, a = stack.pop(), stack.pop()
                stack.append(int(a) * int(b))
            else:
                stack.append(t)
        
        return int(stack[-1])