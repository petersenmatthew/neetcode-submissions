class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        max_volume = 0
        while i < j:
            length = j - i
            cur_volume = min(heights[i], heights[j]) * length
            max_volume = max(cur_volume, max_volume)
            if heights[j] <= heights[i]:
                j -=1
            else:
                i +=1
        return max_volume
    