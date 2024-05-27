# Solution to LeetCode Problem: Two Sum
# https://leetcode.com/problems/two-sum/

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mem = {}
        for i in range(0,len(nums)):
            second_num = target - nums[i]
            if second_num in mem:
                return [mem[second_num], i]
            else:
                mem[nums[i]] = i

        return []

nums = [2,7,11,15]
target = 18

s = Solution() 
print(s.twoSum(nums,target))
