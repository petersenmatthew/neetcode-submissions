class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_letter_occurences = {}

        for i in range(len(s)):
            if s[i] not in s_letter_occurences:
                s_letter_occurences[s[i]] = 1
            else:
                s_letter_occurences[s[i]] += 1
        
        print("s: ", s_letter_occurences)

        t_letter_occurences = {}
        for i in range(len(t)):
            if t[i] not in t_letter_occurences:
                t_letter_occurences[t[i]] = 1
            else:
                t_letter_occurences[t[i]] += 1
        print("t: ", t_letter_occurences)
        for letter in t_letter_occurences:
            if (letter not in s_letter_occurences) or (t_letter_occurences[letter] != s_letter_occurences[letter]):
                return letter


        
