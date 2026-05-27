class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # how is anagram?
        # isAnagram(str1: str, str2: str) -> bool
        # Or we can check if the rotated strings are equal to each other. 
        # .sort - > sort in alphabetical 
        # str1 == str2 - anagram

        output = []

        # hash_map:
        # key : value
        # sorted_str : [strings]
        hash_map = {}
        for string in strs:
            sorted_str = "".join(sorted(string))
            if sorted_str in hash_map:
                hash_map[sorted_str].append(string)
            else:
                hash_map[sorted_str] = [string]
 
        # {act: [act, cat], }

        # output is a list:
        for item in hash_map:
            output.append(hash_map[item])
        return output