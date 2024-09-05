from typing import List


class Solution:
    def countWays(self, nums: List[int]) -> int:
        TotalNums = len(nums)
        resultnum = 0
        sortednums = sorted(nums)
        for happynum in range(0, TotalNums):
            if sortednums[happynum - 1] < happynum and sortednums[happynum] > happynum:
                 print(happynum)
                 resultnum +=1
        if 0 < min(nums):
              resultnum += 1
        if TotalNums > max(nums):
              resultnum += 1
        return resultnum