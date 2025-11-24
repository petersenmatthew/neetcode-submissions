class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def sumString(a: str) -> int:
            string_sum = 0
            power = 0
            for i in range(len(a) - 1, -1, -1):
                if a[i] == '1':
                    string_sum += 2 ** power
                power += 1
            return string_sum
        def numToBinary(num: int) -> str:
            result = ""
            if num == 0:
                return "0"
            while num != 0:
                result += str(num % 2)
                num = num // 2
            return result[::-1]

        print( sumString(a))
        print( sumString(b))
        return (numToBinary( sumString(a) + sumString(b)))       
