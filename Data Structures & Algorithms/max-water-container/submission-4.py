class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        left = 0
        right = len(heights) - 1
        while left < right:
            distance = right - left
            area = min(heights[right], heights[left]) * distance
            maxArea = max(maxArea, area)
            if heights[right] < heights[left]:
                right -=1
            else:
                left+=1
        
        return maxArea
