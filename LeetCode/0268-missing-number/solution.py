class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_range = len(nums)
        print("range: ", num_range)
        for i in range(num_range + 1):
            if i not in nums:
                return i

                # 0 1 
