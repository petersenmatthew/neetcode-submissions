class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # hash map. word : frequency

        banned_set = set(banned)
        
        frequency_map = {}
        punctuation = {"!", "?", "'", ",", ";", ".", " "}

        new_paragraph = ""
        for letter in paragraph:
            if letter in punctuation:
                new_paragraph += " "
            else:
                new_paragraph += letter.lower()

        for word in new_paragraph.split():
            print(word)
            if word not in banned_set:
                if word not in frequency_map:
                    frequency_map[word] = 1
                else:
                    frequency_map[word] += 1

        max_key = max(frequency_map, key=frequency_map.get)
        print (frequency_map)
        return max_key

