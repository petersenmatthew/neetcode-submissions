class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # amount of water = min(heights[l], heights[r]) * (r-l)
        # l, r are two bars
        # l-r is the distance between the two
        best = 0
        l = 0
        for l in range(len(heights)):
            print(heights)
            r = len(heights) - 1
            print(r, heights[r])
            while l < r:  
                x = r - l
                y = min(heights[l],heights[r])
                current = x * y
                print("current:", current, x, y)
                best = max(best,current)
                print("best", best)
                r-=1
        return best