class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == '+':
                num1, num2 = stack.pop(), stack.pop()
                stack.append(int(num1) + int(num2))
            elif t == '-':
                num1, num2 = stack.pop(), stack.pop()
                stack.append(int(num2) - int(num1))
            elif t == '*':
                num1, num2 = stack.pop(), stack.pop()
                stack.append(int(num1) * int(num2))
            elif t == '/':
                num1, num2 = stack.pop(), stack.pop()
                stack.append(int(num2) / int(num1))
            else:
                stack.append(t)

        return int(stack[0])
