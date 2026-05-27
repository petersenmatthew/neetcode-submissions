class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        best = 0
        known = set()
        print(len(s))
        if len(s) < 2:
            return len(s)

        while r < len(s):
            while s[r] in known: # keep going until s[r] is unot nqiue
                known.remove(s[l])
                l += 1
            known.add(s[r])
            best = max(best, r - l + 1)
            r += 1

        return best