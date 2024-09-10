from typing import List

class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        more = [[0] * n for _ in range(n + 1)]
        less = [[0] * n for _ in range(n + 1)]
        for j in reversed(range(n)):
            for k in reversed(range(j + 1, n)):
                if nums[j] < nums[k]:
                    more[k][j] = more[k + 1][j] + 1
                else:
                    more[k][j] = more[k + 1][j]

        for k in range(n):
            for j in range(k):
                if nums[k] > nums[j]:
                    less[j][k] = less[j - 1][k] + 1
                else:
                    less[j][k] = less[j - 1][k]
        
        res = 0
        for k in range(n):
            for j in range(k):
                if nums[k] < nums[j]:
                    res += less[j][k] * more[k][j]
        
        return res