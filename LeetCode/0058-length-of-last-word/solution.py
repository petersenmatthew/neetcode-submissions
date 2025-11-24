class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        longest_length: int = 0
        current_length: int = 0
        word_found = False
        for i in range(len(s) - 1, -1, -1):
            print (s[i])
            if s[i] != " ":
                word_found = True
                print("not whitespace")
                current_length +=1
                if current_length >= longest_length:
                    longest_length = current_length
            else:
                if word_found == True:
                    break
                current_length = 0
        return longest_length


