from functools import reduce

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        if len(strs) == 1:
            #Edge case: only 1 string in list
            return strs[0]

        #Use shortest string as reference
        reference = min(strs, key=len)
        
        # Binary Search
        low = 0
        high = len(reference)
        substring = ""

        while low < high:
            index = (high-low)//2 + low
            substring = reference[:index]
            is_substring_in_all = reduce(lambda prev, s: prev and s.startswith(substring), strs)
            if (is_substring_in_all):
                low = index
            else:
                high = index

        return substring

strs = ["flower","flow","flight"]
print(Solution().longestCommonPrefix(strs))
