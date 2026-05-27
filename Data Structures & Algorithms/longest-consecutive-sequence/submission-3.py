class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        print(hash_set)

        best = 0
        cur = 0
        for num in hash_set:
            # Only start building a sequence if 'num' is the beginning
            if (num - 1) not in hash_set:
                current_streak = 1

                # Increment until the sequence breaks
                while (num + 1) in hash_set:
                    num += 1
                    current_streak += 1

                best = max(best, current_streak)
        return best