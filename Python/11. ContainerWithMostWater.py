from typing import List
import bisect

class Solution:
    def maxArea(self, height: List[int]) -> int:
        #1. Build hashtable sorted by height {height : index}
        hi_map:dict[int:list[int]] = {}
        for i in range(len(height)):
            h:int = height[i]
            if h in hi_map:
                hi_map[h].append(i)
            else:
                hi_map[h] = [i]

        #2. For each height, find min and max index. Calc and compare areas.
        h_desc:list[int] = sorted(hi_map.keys(), reverse = True)
        
        max_area = 0
        prev_i:list[int] = []
        for h in h_desc:
            ls_i:list[int] = hi_map[h]
            for i in ls_i:
                bisect.insort(prev_i, i)
            if len(prev_i) < 2:
                # Need two lines to be meaningful
                continue
            w:int = prev_i[-1] - prev_i[0]
            area:int = h * w
            if area > max_area:
                max_area = area
        return max_area

print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))

            