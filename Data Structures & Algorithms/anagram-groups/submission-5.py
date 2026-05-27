class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            anagram_map = {}

            # sort version
            # n * m log m run time
            # n  

            for string in strs:
                count = [0] * 26 # one for each char a - z 

                for char in string:
                    value = ord(char) - ord('a')
                    count[value] += 1
                
                tuple_count = tuple(count)
                if tuple_count in anagram_map:
                    anagram_map[tuple_count].append(string)
                else:
                    anagram_map[tuple_count] = [string]
            
            return list((anagram_map.values()))
            '''
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
            '''