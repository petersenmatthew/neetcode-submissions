class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        a, b = 1, 2  # f(1)=1, f(2)=2
        for _ in range(3, n+1):
            a, b = b, a + b  # f(n) = f(n-1) + f(n-2)
        return b
# n = 1 
# 1 

# n = 2
# 1 + 1
# 2 

# n = 4
# 1 + 1 + 1 + 1 
# 1 + 1 + 2 
# 1 + 2 + 1
# 2 + 1 + 1 
# 2 + 2

# n = 5
# 1 + 1 + 1 + 1 + 1
# 1 + 1 + 1 + 2
# 1 + 1 + 2 + 1
# 1 + 2 + 1 + 1
# 2 + 1 + 1 + 1
# 2 + 2 + 1
# 2 + 1 + 2
# 1 + 2 + 2

# a(n-1) + 2

# 1, 2, 3, 5, 8, 12
# Differneces (+)
# 1, 1, 2, 3, 4, 5

# 1, 2, 3, 4, 5, 6

