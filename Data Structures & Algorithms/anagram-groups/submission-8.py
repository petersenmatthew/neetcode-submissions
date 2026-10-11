class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            anagram_map = {}

            for word in strs:
                # how to tell if two words are an anagram?
                freq = [0] * 26
                for letter in word:
                    ord_value = ord(letter) - 97 # a is 97, z is 122
                    freq[ord_value] += 1
                freq_tuple = tuple(freq)

                if freq_tuple not in anagram_map: 
                    anagram_map[freq_tuple] = []
                anagram_map[freq_tuple].append(word)

            output = []

            for anagram_list in anagram_map.values():
                output.append(anagram_list)

            return output