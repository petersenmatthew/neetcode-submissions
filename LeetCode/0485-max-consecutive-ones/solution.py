class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current_max = 0
        total_max = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                current_max += 1
                if current_max >= total_max:
                    total_max = current_max
            else:
                current_max = 0
        return total_max
