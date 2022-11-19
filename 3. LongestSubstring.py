class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp = ""
        max_len = 0

        for c in s:
            #Idea: Filter substring such that there is no repeating characters.
            temp = temp[temp.index(c)+1:] + c if (c in temp) else temp + c
            max_len = max(len(temp), max_len)

        return max_len

print(Solution().lengthOfLongestSubstring("abcabcbb"))