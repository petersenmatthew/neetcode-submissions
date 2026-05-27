class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        #s1: abc
        #s2: abdcab
        # Sliding window of fixed size of in this one. 

        if len(s2) < len(s1):
            return False
        
        l = 0
        r = len(s1) - 1

        # initalize current window and base
        window = [0] * 26
        base_string = [0] * 26
        for i in range(len(s1)):
            base_string_idx = ord(s1[i]) - ord("a")
            base_string[base_string_idx] += 1

            char_index = ord(s2[i]) - ord("a")
            window[char_index] += 1
        print(window, base_string)

        if window == base_string:
            return True
        
        for i in range(len(s1), len(s2)):
            # Add the new character on the right
            window[ord(s2[i]) - ord('a')] += 1
            # Remove the character that is no longer in the window (left side)
            window[ord(s2[i - len(s1)]) - ord('a')] -= 1
            
            # Check if the counts match
            if window == base_string:
                return True
        return False