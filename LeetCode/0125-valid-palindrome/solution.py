class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove chars from string, set lower
        final_string = ""
        for i in range(len(s)):
            if s[i].isalnum():
                final_string += s[i].lower()
        if final_string == final_string[::-1]:
            return True
        else:
            return False
        print(final_string)
