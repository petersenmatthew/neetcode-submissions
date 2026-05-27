class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_streak = 0

        for num in num_set:
            # ONLY start counting if this is the beginning of a sequence
            if (num - 1) not in num_set:
                current_num = num
                current_streak = 1

                # Use a while loop to 'exhaust' this specific sequence
                while (current_num + 1) in num_set:
                    current_num += 1
                    current_streak += 1
                
                # Update the global max after the while loop finishes
                max_streak = max(max_streak, current_streak)
                
        return max_streak