class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def pal(left:str, result:str, right:str) -> str:
            while left and right:
                if left[-1] != right[0]:
                    break
                result = left[-1] + result + right[0]
                left = left[:-1]
                right = right[1:]
            return result

        s += "!"
        best_string = s[0]

        for i in range(len(s)-2):
            str_doub = pal(s[:i+1], "", s[i+1:]) if s[i] == s[i+1] else ""
            str_single = pal(s[:i+1], s[i+1], s[i+2:]) if s[i] == s[i+2] else ""
            if (len(str_doub) > len(best_string)):
                best_string = str_doub
            if (len(str_single) > len(best_string)):
                best_string = str_single

        return best_string

print(Solution().longestPalindrome("bbb"))