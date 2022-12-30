class Solution:

    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        # 1 + 3 pointer search: building on 3 sum
        # Assume sorted array
        # Idea: fix 1 pt from left, conduct 3sum on the right side of array.

        result:list[list[int]] = list()

        def threeSum(s:int, tar:int) -> None:
            # 1 + 2 pointer search: building on 2 sum
            # Idea: fix 1 pt from left, conduct 2sum on the right side of array.

            def twoSum(s:tar, tar:int) -> None:

                if nums[s] > tar//2 or nums[-1] < tar//2:
                    return

                e:int = len(nums)-1
                while s < e:
                    third:int = nums[s]
                    fourth:int = nums[e]
                    sum:int = third + fourth
                    if sum < tar:
                        s += 1
                        while s < e and nums[s] == nums[s-1]:
                            s += 1
                    elif sum == tar:
                        result.append([first, second, third, fourth]) 
                        s += 1
                        while s < e and nums[s] == nums[s-1]:
                            s += 1
                    else:
                        e -= 1
                        while s < e and nums[e] == nums[e+1]:
                            e -= 1
            
            if nums[s] > tar//3 or nums[-1] < tar//3:
                return

            while s < len(nums)-2:
                second:int = nums[s]
                twoSum(s = s+1, tar = tar - second)
                s += 1
                while s < len(nums)-2 and nums[s] == nums[s-1]:
                    s += 1

        nums.sort()
        s:int = 0
        while s < len(nums)-3:
            first:int = nums[s]
            threeSum(s = s+1, tar = target - first)
            s += 1
            while s < len(nums)-3 and nums[s] == nums[s-1]:
                s += 1
        return result

print(Solution().fourSum([2,2,2,2,2], 8))
