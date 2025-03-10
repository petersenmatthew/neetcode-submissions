class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransomdict = {}
        magazinedict = {}
        # iterate throug heach letter in ransomnote
        for char in ransomNote:
            # if letter is new, add to dictionary with letter: 1
            if char not in ransomdict:
                ransomdict[char] = 1
            else:
                ransomdict[char] += 1
        for char in magazine:
            # if letter is new, add to dictionary with letter: 1
            if char not in magazinedict:
                magazinedict[char] = 1
            else:
                magazinedict[char] += 1

        for key in ransomdict.keys():
            if ransomdict.get(key) > magazinedict.get(key):
                return False

        return True
        # compare both dicitonaries
        # for each letter in ransomdictionary, correspondant in magazinedic must be equal or greater
        # if so, return true
        # else, return false
