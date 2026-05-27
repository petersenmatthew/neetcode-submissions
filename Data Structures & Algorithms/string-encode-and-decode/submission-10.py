class Solution:
    from typing import List
    #input : list of strings
    # outpit: one string
    def encode(self, strs: List[str]) -> str:
        output_str = ""
        for word in strs:
            length = str(len(word))
            output_str += length + "#" + word 
        print(output_str)
        return(output_str)
    
    def decode(self, s: str) -> List[str]:
        i = 0
        word_list = []
        while i < len(s):
            hash_loc = s.index("#", i)
            cur_word_length = int(s[i:hash_loc]) # word length is until first #
            print("hash @", hash_loc, "word length:", cur_word_length)
            word = s[i + (hash_loc - i + 1):cur_word_length + hash_loc + 1]
            print("word found:", word)
            word_list.append(word)
            print("word list", word_list)
            i = cur_word_length + (hash_loc - i) + 1 + i
            print("new i", i)
        return word_list


        # 5#hello3#bye
        # 01234567891011

        # word = s[4 + 6]