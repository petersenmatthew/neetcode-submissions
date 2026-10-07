class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0

        window = {}
        max_window = 0
        for right in range(len(s)):
            # how to know which is the dominant character?
            # while characters that arent dominant > k:
            # move left
            window_size = right - left + 1
            window[s[right]] = window.get(s[right], 0) + 1

            max_count = max(window.values())
            replacements_needed = window_size - max_count
            while replacements_needed > k:
                window[s[left]] -= 1
                left +=1
                window_size = right - left + 1
                replacements_needed = window_size - max_count
            max_window = max(max_window, window_size)
        return max_window