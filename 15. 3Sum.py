class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # 1 + 2 pointer search: building on 2 sum
        # Assume sorted array
        # Idea: fix 1 pt from left, conduct 2sum on the right side of array.

        result:list[list[int]] = list()

        def twoSum(tar:int, s:int, e:int = len(nums) - 1):
            while s < e:
                first:int = nums[s]
                second:int = nums[e]
                sum:int = first + second
                if sum < tar:
                    s += 1
                    while s < e and nums[s] == nums[s-1]:
                        s += 1
                elif sum == tar:
                    result.append([first, second, -tar]) 
                    s += 1
                    while s < e and nums[s] == nums[s-1]:
                        s += 1
                else:
                    e -= 1
                    while s < e and nums[e] == nums[e+1]:
                        e -= 1

        nums.sort()
        i:int = 0
        while i < len(nums)-2:
            first:int = nums[i]
            twoSum(-first, i+1, len(nums)-1)
            i += 1
            while i < len(nums)-2 and nums[i] == nums[i-1]:
                i += 1
        return result

nums = [0,0,0]

print(Solution().threeSum(nums))



                




