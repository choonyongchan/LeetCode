class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Use fast exp algo
        if (n < 0):
            x = 1 / x
        result:int = 1
        while n != 0:
            if n % 2:
                result *= x
            n = int(n/2)
            x *= x
        return result 