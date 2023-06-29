# https://leetcode.com/problems/remove-duplicates-from-sorted-array/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        prev = nums[0]
        unq = 1
        pos = 0

        for i in range(1, len(nums)):
            if nums[i] != prev:
                unq += 1
                prev = nums[i]
                pos += 1
            
            nums[pos] = nums[i]
        
        return unq


nums = [0,0,1,1,1,2,2,3,3,4]
print(nums)
sol = Solution()
res = sol.removeDuplicates(nums)
print(nums)
print(nums[:res])
            

