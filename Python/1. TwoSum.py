class Solution:

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        ##Solution 2: Two pointer search

        #Step 1: Sort indices for Binary Search
        indices = sorted(range(len(nums)), key=lambda k: nums[k])
        
        #Step 2: Two pointer search
        firstI = 0
        lastI = len(nums)-1

        while firstI < lastI:
            sum = nums[indices[firstI]] + nums[indices[lastI]]
            if (sum == target):
                return [indices[firstI], indices[lastI]]
            elif (sum < target):
                firstI += 1
            else:
                lastI -= 1
        
        raise ValueError("No pairs")

print(Solution().twoSum([-10,-1,-18,-19], -19))


"""
Solution 1: Using Dictionary

def twoSum(self, nums: List[int], target: int) -> List[int]:
    # Init Index-Value Dictionary
    numDict:dict = {}
    for i in range(len(nums)):
        num = nums[i]
        #Check values
        secondI = numDict.get(target - num)
        if (secondI):
            return [secondI[0], i]

        if num in numDict.keys():
            numDict[num].append(i)
        else:
            numDict[num] = [i]
"""
