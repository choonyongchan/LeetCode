class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        repl_idx:int = 1 # Pointer to replace values in list

        for curr_val in nums[1:]: # Pointer to current value
            if curr_val != nums[repl_idx-1]:
                nums[repl_idx] = curr_val
                repl_idx += 1
        
        return repl_idx

nums = [0,0,1,1,1,2,2,3,3,4]
print(Solution().removeDuplicates(nums))
print(nums)