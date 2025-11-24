class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row = "qwertyuiop"
        second_row = "asdfghjkl"
        third_row = "zxcvbnm"

        rows = [first_row, second_row, third_row]
        fits = True
        answer = []
        used_row = 0
        for word in words:
            print("Word: ", word)
            lower_word = word.lower()

            fits = True  # assume the word fits until proven otherwise
            # find which row the first letter is in
            for j in range(len(rows)):
                if lower_word[0] not in rows[j]:
                    print("Letter: ", lower_word[0], "not in ", rows[j])
                    pass
                else:
                    print("Letter: ", lower_word[0], "IS in ", rows[j]) 
                    used_row = j

            # iterate over all other letters
            for i in range(1, len(lower_word)):
                if lower_word[i] not in rows[used_row]:
                    fits = False
                    break
                else:
                    fits = True
            if fits == True:
                answer.append(word)
                # find where the first letter is,
                # all subsequent letters of that word must be in that row
        return answer
