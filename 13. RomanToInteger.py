from multiprocessing.sharedctypes import Value


class Solution:

    def romanToInt(self, s: str) -> int: 
        # Proposed Solution: Read two chars at a time. 
        # When special combos appear, skip two chars,
        # else skip one char.

        class CharTuple:
            def __init__(self, first:str, second:str):
                self.first = first
                self.second = second

            def findCombo(self):
                if (self.first == "I" and self.second == "V"):
                    return 4
                if (self.first == "I" and self.second == "X"):
                    return 9
                if (self.first == "X" and self.second == "L"):
                    return 40
                if (self.first == "X" and self.second == "C"):
                    return 90
                if (self.first == "C" and self.second == "D"):
                    return 400
                if (self.first == "C" and self.second == "M"):
                    return 900
                return 0
            
            def findSum(self):
                target:str = self.first
                if (target == "I"):
                    return 1
                if (target == "V"):
                    return 5
                if (target == "X"):
                    return 10
                if (target == "L"):
                    return 50
                if (target == "C"):
                    return 100
                if (target == "D"):
                    return 500
                if (target == "M"):
                    return 1000
                raise ValueError

            def updateOne(self, new:str):
                return CharTuple(self.second, new)
            
            def updateBoth(self, first:str, second:str):
                return CharTuple(first, second)
               
        
        def splitChars(s:str) -> list[str]:
            return list(s)

        chars:list[str] = splitChars(s)
        length = len(chars)
        chars.append(" ") #end marker
        sum:int = 0
        index:int = 1

        while index <= length:
            currTuple:CharTuple = CharTuple(chars[index-1], chars[index])
            
            comboSum:int = currTuple.findCombo()
            if comboSum > 0:
                index += 2
                sum += comboSum
                continue

            normalSum:int = currTuple.findSum()
            index += 1
            sum += normalSum
        
        return sum

print(Solution().romanToInt("MCMXCIV"))
        
