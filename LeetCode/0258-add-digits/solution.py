class Solution:
    def addDigits(self, num: int) -> int:
        def sum_of_digits(number):
            digits = [int(digit) for digit in str(number)]
            total_sum = 0
            for i in range(len(digits)):
                total_sum += digits[i]
            return total_sum
        

        result = sum_of_digits(num)
        while len(str(result)) != 1:
            result = sum_of_digits(result)

        return result
