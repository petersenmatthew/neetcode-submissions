class Solution:
    def findMin(self, nums: List[int]) -> int:
        # n means that the 
        l, r = 0, len(nums) - 1
        lowest = float("infinity")
        while l <= r:
            mid = (l + r) // 2
            lowest = min(lowest, nums[mid])
            if nums[mid] < nums[r]:
                r = mid - 1
            else:
                l = mid + 1
        return lowest