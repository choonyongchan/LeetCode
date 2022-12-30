class Solution:

    MAPPING:list[tuple[str]] = [
        ("a", "b", "c"), 
        ("d", "e", "f"),
        ("g", "h", "i"),
        ("j", "k", "l"),
        ("m", "n", "o"),
        ("p", "q", "r", "s"),
        ("t", "u", "v"),
        ("w", "x", "y", "z")
    ]

    def letterCombinations(self, digits: str) -> list[str]:
        
        if not digits:
            return 
        digits:int = int(digits)
        result:list[str] = []
        
        while digits != 0:
            last:int = digits % 10
            digits //= 10
            alphabets:tuple[str] = Solution.MAPPING[last-2]
            result = [a+r for r in result for a in alphabets] if result else list(alphabets)
        
        return result

digits = "23"
print(Solution().letterCombinations(digits))