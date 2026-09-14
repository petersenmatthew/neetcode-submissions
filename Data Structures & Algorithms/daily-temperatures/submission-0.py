class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):

            while len(stack) != 0 and temperatures[stack[-1]] < temp:
                previous_day = stack.pop()
                result[previous_day] = i - previous_day

            stack.append(i)

        return result