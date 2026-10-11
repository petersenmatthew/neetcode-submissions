class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        best = 0 
        cur = 0
        # define a set with all nums
        for num in nums_set:
            if num - 1 not in nums_set:
                # is a start
                cur = 1
                while num + 1 in nums_set:
                    cur += 1
                    num += 1
                best = max(cur, best)

        return best
                