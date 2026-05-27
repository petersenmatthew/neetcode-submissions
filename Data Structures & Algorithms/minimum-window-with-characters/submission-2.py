class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_T, window = {}, {}
        # key : value
        # char : frequency

        l = 0
        count = 0
        min_len = float('inf')
        res = ""

        for char in t:
            count_T[char] = 1 + count_T.get(char, 0)

        print(count_T)

        have, need = 0, len(count_T)
        res, resLen = [-1, -1], float("infinity")
        for r in range (len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            if c in count_T and window[c] == count_T[c]:
                have+=1 
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                window[s[l]] -= 1
                # 3. If we just lost a 'needed' character, decrement 'have'
                if s[l] in count_T and window[s[l]] < count_T[s[l]]:
                    have -= 1
                l += 1
        
        return(s[res[0]: res[1] + 1])