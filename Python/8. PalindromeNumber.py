class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False

        ori:int = x
        rev:int = 0
        while ori != 0:
            rev = (rev * 10) + ori % 10
            ori //= 10
        return x == rev
        



        


