from collections import deque
from typing import List


class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        ans = s = left = 0
        q = deque()
        for right, (t, c) in enumerate(zip(chargeTimes, runningCosts)):
            while q and t >= chargeTimes[q[-1]]:
                q.pop()
            q.append(right)
            s += c

            while q and chargeTimes[q[0]] + (right - left + 1) * s > budget:
                if q[0] == left:
                    q.popleft()
                s -= runningCosts[left]
                left += 1

            ans = max(ans, right - left + 1)
        return ans