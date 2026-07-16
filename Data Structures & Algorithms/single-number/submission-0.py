class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = dict()
        t = 0
        for i in nums:
            s = seen.get(i, 0)
            if s == 0:
                seen[i] = 1
                t += i
                
            else:
                seen[i] -= 1
                t -= i
        return t
        