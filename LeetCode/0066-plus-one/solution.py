class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        last_digit = digits[len(digits) - 1]
        if last_digit == 9:
            for i in range(len(digits) - 1, -1, -1):
                if digits[i] != 9:
                    digits[i] += 1
                    break
                elif i == 0 and digits[i] == 9:
                    digits[i] = 1
                    digits.append(0)

            for j in range(i+1, len(digits)):
                digits[j] = 0
        else:
            digits[len(digits) - 1] +=1

        return digits

[9, 9]

[9, 9, 9]

[1, 9, 9]
