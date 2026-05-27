class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hashmap - sorted_string : anagram formations

        hashmap = {}
        for index, string in enumerate(strs):
            sorted_string_list = sorted(string)
            print(sorted_string_list) # will be in list of characters
            sorted_string = "".join(sorted_string_list)    # Result: "aet"
            print(sorted_string)

            if sorted_string in hashmap:
                hashmap[sorted_string].append(strs[index])
            else:
                hashmap[sorted_string] = [strs[index]]
    
        print(hashmap)
        return list(hashmap.values())

