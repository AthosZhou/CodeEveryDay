from typing import List

class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums = sorted(nums)
        i = 0
        for head in nums[(len(nums)+1) //2:]:
            if nums[i] * 2 <= head:
                i+=1
        return i * 2