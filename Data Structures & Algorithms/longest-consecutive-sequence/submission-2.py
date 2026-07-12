class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        c = 1
        m = 1
        s = sorted(list(set(nums)))
        for i in range(1, len(s)):
            if s[i] - s[i-1] == 1:
                c += 1
                if c > m:
                    m = c
            else:
                if c > m:
                    m = c
                c = 1
        return m
            
                