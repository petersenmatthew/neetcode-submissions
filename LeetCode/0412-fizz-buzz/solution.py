class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        answer = []
        for i in range(n + 1):
            if i > 0:
                print(i)
                if (i % 3 == 0) and (i % 5 == 0):
                    answer += ["FizzBuzz"]
                elif (i % 3 == 0):
                    answer += ["Fizz"]
                elif (i % 5 == 0):
                    answer += ["Buzz"]
                else:
                    answer += [str(i)]
        return answer
