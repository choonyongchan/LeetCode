from typing import List

class Solution:
    def convert(self, s: str, numRows: int) -> str:

        result:List[List[int]] = ["" for _ in range(numRows)]
        curr_row:int = 0
        isDown:bool = True

        while s:
            result[curr_row] += s[0]
            s = s[1:]

            if numRows == 1:
                pass
            elif isDown:
                curr_row += 1
            else:
                curr_row -= 1

            if (curr_row == numRows - 1):
                isDown = False
            if (curr_row == 0):
                isDown = True

        return(''.join(result))

print(Solution().convert("ABCDEFG", 2))
            
            

