class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {
            "}" : "{",
            "]" : "[",
            ")" : "("
        }

        stack = []
        for bracket in s:
            if bracket not in close_to_open: # open bracket
                stack.append(bracket)
            else: # close bracket
                if not stack or stack[-1] != close_to_open[bracket]:
                    return False
                else:
                    stack.pop()
        
        return len(stack) == 0
    