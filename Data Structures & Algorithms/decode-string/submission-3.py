class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        result = ""
        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])

            else: # is a closing bracket
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop()
                
                multiplier = ""
                while len(stack) > 0 and stack[-1].isdigit():
                    multiplier = stack.pop() + multiplier
                multiplier = int(multiplier)

                substr = substr * multiplier

                stack.append(substr)

        return "".join(stack)
