class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        best = 0
        for num in nums_set:
            if num - 1 not in nums_set:  # Is num the START of a sequence?
                cur = 1
                next_num = num + 1

                while next_num in nums_set:  # Does the next number exist?
                    cur += 1
                    next_num += 1

                best = max(best, cur)

        return best