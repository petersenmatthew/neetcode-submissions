class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        known_nums = []
        for num in nums:
            if num in known_nums:
                return True
            known_nums.append(num)

        return False
