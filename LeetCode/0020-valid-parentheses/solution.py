class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {
            "}" : "{",
            ")" : "(",
            "]" : "["
        }
        stack = []
        for i in range(0, len(s)):
            if s[i] in bracket_map:
                if stack and stack[-1] == bracket_map[s[i]]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
        if len(stack) == 0:
            return True
        else:
            return False
