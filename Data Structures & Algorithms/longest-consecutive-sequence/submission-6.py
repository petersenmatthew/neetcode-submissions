class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        best = 0 
        cur = 0
        for num in nums_set:
            # need to num if osomething is the start of a euquence
            if (num - 1) not in nums_set:
                # num is the start of a seuquence
                cur = 1 

                # ...
                while num + 1 in nums_set:
                    cur += 1
                    num += 1

                best = max(cur, best)

        return best