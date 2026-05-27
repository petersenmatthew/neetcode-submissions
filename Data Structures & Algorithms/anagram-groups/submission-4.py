class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            anagram_map = {}
            for string in strs:
                sorted_string = ''.join(sorted(string))
                if sorted_string in anagram_map:
                    anagram_map[sorted_string].append(string)
                else:
                    anagram_map[sorted_string] = [string]
            print(anagram_map)

            output = []

            for group in anagram_map.values():
                output.append(group)
            return output