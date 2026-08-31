class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == "+":
                b = stack.pop()
                a = stack.pop()
                # pop 2 values, add them, and append
                stack.append(a+b)

            elif token == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a-b)

            elif token == "*":
                b = stack.pop()
                a = stack.pop()
                stack.append(a*b)

            elif token == "/":
                b = stack.pop()
                a = stack.pop()
                # pop 2 values, add them, and append
                stack.append(int(a/b))
            else:
                # token must be a number
                stack.append(int(token))
        
        return stack[-1]