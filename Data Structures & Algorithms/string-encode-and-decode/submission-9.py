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
        s_length = len(s)
        word_list = []
        while i < s_length:
            hash_loc = s.index("#")
            print("hash loc", hash_loc)
            cur_word_length = int(s[:hash_loc]) # word length is until first #
            print("cur word length", cur_word_length)
            word = s[(hash_loc + 1):cur_word_length + hash_loc + 1]
            word_list.append(word)
            s = s[(cur_word_length + hash_loc + 1):]
            s_length = len(s)
            print(word_list)
            print("i", i, "s length", s_length, "s: ", s)
        return word_list


        # 5#hello