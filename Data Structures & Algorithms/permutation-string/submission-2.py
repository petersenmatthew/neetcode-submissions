class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        freq_map = {}
        for char in s1:
            if char not in freq_map:
                freq_map[char] = 0
            freq_map[char]+=1
        
        l = 0
        r = len(s1) - 1

        cur_map = {}

        for i in range(r + 1):
            char = s2[i]
            if char not in cur_map:
                cur_map[char] = 0
            cur_map[char]+=1 
        if cur_map == freq_map:
            return True

        while r < len(s2) - 1:
            cur_map[s2[l]] -=1
            if cur_map[s2[l]] == 0:
                del cur_map[s2[l]]


            l+=1 
            r+=1
            if s2[r] not in cur_map:
                cur_map[s2[r]] = 0
            cur_map[s2[r]] +=1
        
            if cur_map == freq_map:
                return True
        return False
