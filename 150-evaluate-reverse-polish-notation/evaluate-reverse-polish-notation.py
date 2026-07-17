class Solution:
    def evalRPN(self, tokens: list) -> int:  # Or simply remove ': list' entirely
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))  # Cleaned up the float() cast too!
            else:
                stack.append(int(c))
        return stack[0]