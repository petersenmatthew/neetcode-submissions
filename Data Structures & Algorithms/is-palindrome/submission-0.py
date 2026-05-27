class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        s = s.lower()
        
        while l < r:
            # Skip non-alphanumeric from the left
            while l < r and not s[l].isalnum():
                l += 1
            # Skip non-alphanumeric from the right
            while l < r and not s[r].isalnum():
                r -= 1
            
            # Actual comparison
            if s[l] != s[r]:
                return False
            
            l += 1
            r -= 1
            
        return True