class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        for i, num in enumerate(nums):
            m = 1
            for j, num2 in enumerate(nums):
                if i == j:
                    continue
                m *= num2
            ans.append(m)
        return ans