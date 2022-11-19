from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # Algorithm to be improved
        
        len1:int = len(nums1)
        len2:int = len(nums2)
        
        #Ensure len(nums1) <= len(nums2)
        if len1 > len2:
            nums1, nums2 = nums2, nums1
            len1, len2 = len2, len1
        
        low:int = 0
        high:int = len1

        while low <= high:

            part1:int = int((low + high) / 2)
            part2:int = int((len1 + len2 + 1) / 2 - part1)

            part1l:int = nums1[part1 - 1] if part1 != 0 else float("-inf")
            part1r:int = nums1[part1] if part1 != len1 else float("inf")

            part2l:int = nums2[part2 - 1] if part2 != 0 else float("-inf")
            part2r:int = nums2[part2] if part2 != len2 else float("inf")

            if (part1l > part2r):
                high = part1 - 1
                continue
            if (part2l > part1r):
                low = part1 + 1
                continue
            

            if (len1 + len2) % 2:
                return max(part1l, part2l)
            else:
                return (max(part1l, part2l) + min(part1r, part2r)) / 2

        raise ValueError


print(Solution().findMedianSortedArrays([1,3], [2]))

    