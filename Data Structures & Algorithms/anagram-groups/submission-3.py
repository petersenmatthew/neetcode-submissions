class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            anagram_map = {}
        
            for s in strs:
                count = [0] * 26 
                for char in s:
                    count[ord(char) - ord('a')] += 1
                
                key = tuple(count)
                
                # Manually check if the key is missing
                if key not in anagram_map:
                    anagram_map[key] = []
                    
                anagram_map[key].append(s)
            
            return(list(anagram_map.values()))