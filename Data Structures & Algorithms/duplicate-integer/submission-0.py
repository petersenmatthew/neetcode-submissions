class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        known_nums = []
        for num in nums:
            if num in known_nums:
                return True
            else:
                known_nums.append(num)

        return False
