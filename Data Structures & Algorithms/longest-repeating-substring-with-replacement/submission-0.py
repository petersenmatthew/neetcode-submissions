class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash_map = {}
        # key : value
        # character : frequency

        l, r = 0, 0
        best = 0
        max_f = 0
        # window = l - r + 1
        while r < len(s):
            current_char = s[l]
            if s[r] not in hash_map:
                hash_map[s[r]] = 1
            else:
                hash_map[s[r]] += 1
            max_f = max(max_f, hash_map[s[r]])

            while (r - l + 1) - max_f > k:
                hash_map[s[l]] -= 1
                l += 1
            best = max(best,(r - l + 1))
            r+=1
        return best