class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                # [1, 2]
                # perform the operation, and then append the result
                stack.append(int(stack.pop()) + int(stack.pop()))
            elif token == "-":
                top = stack.pop()
                second = stack.pop()
                stack.append(int(second) - int(top))
            elif token == "*":
                stack.append(int(stack.pop()) * int(stack.pop()))
            elif token == "/":
                top = stack.pop()
                second = stack.pop()
                stack.append(int(second) / int(top))
            else: # normal char
                stack.append(token)
        
        return int(stack[-1])