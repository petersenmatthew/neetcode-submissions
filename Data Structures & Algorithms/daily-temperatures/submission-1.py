class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        output = [0] * len(temperatures)
        # [71, 72, 70, 69, 75]
        
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                # temperature found that is greater for others
                output[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return output