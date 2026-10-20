class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
                
        frequency_map = {}

        left = 0
        right = 0
        best = 0
        while right < len(s):
            cur = s[right]
            
            if cur not in frequency_map:
                frequency_map[cur] = 0
            frequency_map[cur] += 1
            
            max_freq = max(frequency_map.values())
            # find # of non_dominant characters
            # = window_size - max_freq

            non_dominant = right - left + 1 - max_freq
            while non_dominant > k:
                frequency_map[s[left]] -= 1
                left += 1

                max_freq = max(frequency_map.values())
                non_dominant = right - left + 1 - max_freq
            
            window_size = right - left + 1
            max_freq = max(frequency_map.values())
            best = max(window_size, best)
            right += 1
        return best
            