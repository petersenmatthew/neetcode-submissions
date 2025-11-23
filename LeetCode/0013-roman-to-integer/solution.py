class Solution:
    def romanToInt(self, s: str) -> int:
        result: int = 0
        roman_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        i = 0
        for char in s:
            result += roman_map[char]
            print(result)
            print("I: ", i)
            print("Length: ", len(s))
            if i < len(s) - 1:
                if char == "I" and (s[i + 1] == "V" or s[i + 1] == "X"):
                    result -= 2
                elif char == "X" and (s[i + 1] == "L" or s[i + 1] == "C"):
                    result -= 20
                elif char == "C" and (s[i + 1] == "D" or s[i + 1] == "M"):
                    result -= 200
            i+=1
        return result
