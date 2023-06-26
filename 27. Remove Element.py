# https://leetcode.com/problems/remove-element/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        pos = 0
        found = 0

        for i in range(len(nums)):
            nums[pos] = nums[i]

            if nums[i] != val:
                pos += 1
            else:
                found += 1
            
        
        return len(nums) - found


nums = [0,1,2,2,3,0,4,2]
print(nums)
val = 2
sol = Solution()
res = sol.removeElement(nums, val)
print(nums, res, sep="\n")