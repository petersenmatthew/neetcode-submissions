class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Find the smallest length word
        min_length = min(len(s) for s in strs)

        common_prefix = ""

        # Loop over each character index
        for i in range(min_length):
            # Take the character from the first string as reference
            ch = strs[0][i]

            # Check if all words match this character
            for j in range(1, len(strs)):
                if strs[j][i] != ch:
                    return common_prefix

            # If all match, add to prefix
            common_prefix += ch

        return common_prefix
# loops:
# outer: loop over every character [i] of each string
# inner: loop over every string in list
