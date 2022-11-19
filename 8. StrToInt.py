class Solution:
    def myAtoi(self, s: str) -> int:
        s:str = s.strip()
        if not s:
            return 0
        isNeg:bool = (s[0] == "-")
        if s[0] == "-" or s[0] == "+":
            s:str = s[1:]
        num:int = 0
        while s and s[0].isdigit():
            digit:int = int(s[0])
            num:int = num * 10 + digit
            s:str = s[1:]
        if isNeg:
            num:int = -num
        if num < -(2**31):
            return -(2**31)
        if num > (2**31)-1:
            return (2**31)-1
        return num

print(Solution().myAtoi("     -42"))