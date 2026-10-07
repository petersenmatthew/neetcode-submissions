class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        left = 0

        longest_length = 0
        for right in range(len(s)):
            while s[right] in chars:
                chars.remove(s[left])
                left += 1

            chars.add(s[right])
            cur_length = right - left + 1 
            longest_length = max(cur_length, longest_length)
        return longest_length
