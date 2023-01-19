class Solution:
    def reverse(self, x: int) -> int:
        if not -(1<<31) <= x <= (1<<31)-1:
            return 0
        x_abs = abs(x)
        rev:int = 0
        while x_abs != 0:
            rev = rev * 10 + (x_abs % 10)
            x_abs //= 10
        if not -(1<<31) <= rev <= (1<<31)-1:
            return 0
        return -rev if x<0 else rev
        
print(Solution().reverse(-1234))