class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hashmap - sorted_string : anagram formations

        hash_map = {}
        for string in strs:
            sorted_string = "".join(sorted(string))
            if sorted_string not in hash_map:
                hash_map[sorted_string] = [string]
            else:
                hash_map[sorted_string].append(string)
        
        print(hash_map)
        return (list((hash_map.values())))