class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_count = {}
        for letter in s:
            if letter in s_count:
                s_count[letter] += 1;
            else:
                s_count[letter] = 1;
        
        print(s_count)

        for letter in t:
            if letter in s_count.keys() and (s_count[letter] > 0):
                s_count[letter] -= 1;
        print("new s count", s_count)
        value_sum = 0

        for value in s_count.values():
            value_sum += value;
        
        print(value_sum)
        if value_sum == 0:
            return True
        return False