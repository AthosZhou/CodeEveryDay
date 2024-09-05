class Solution:
    def clearDigits(self, s: str) -> str:
        for idx in range(len(s)):
            if s[idx].isdigit():
                return self.clearDigits(s[:idx-1]+s[idx+1:])
        return s