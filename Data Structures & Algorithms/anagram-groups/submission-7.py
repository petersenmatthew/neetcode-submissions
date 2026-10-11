class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            anagram_map = {}

            for word in strs:
                # how to tell if two words are an anagram?
                sorted_word = "".join(sorted(word))
                # Cba -> abc

                if sorted_word not in anagram_map: 
                    anagram_map[sorted_word] = []
                anagram_map[sorted_word].append(word)

            output = []

            for anagram_list in anagram_map.values():
                output.append(anagram_list)

            return output