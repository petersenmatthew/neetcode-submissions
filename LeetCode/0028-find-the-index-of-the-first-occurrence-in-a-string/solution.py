class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0  # haystack index
        j = 0  # needle index
        
        while i < len(haystack):
            if haystack[i] == needle[j]:
                # Characters match, move both forward
                i += 1
                j += 1
                
                # If j reached the end of needle, we found it
                if j == len(needle):
                    return i - j
            else:
                # Mismatch occurred
                # We must backtrack i to the character AFTER where the current match started
                # The current match started at (i - j), so we go to (i - j + 1)
                i = i - j + 1
                
                # Reset j to the start of the needle
                j = 0
                
        return -1
