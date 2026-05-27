class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        s = s.lower()

        def isValid(s: str) -> bool:
            if 48 <= ord(s) <= 57 or 65 <= ord(s) <= 90 or 97 <= ord(s) <= 122:
                return True
            else:
                return False

        while l < r:
            # Skip non-alphanumeric from the left
            while l < r and not isValid(s[l]):
                l += 1
            # Skip non-alphanumeric from the right
            while l < r and not isValid(s[r]):
                r -= 1
            
            # Actual comparison
            if s[l] != s[r]:
                return False
            
            l += 1
            r -= 1
            
        return True

