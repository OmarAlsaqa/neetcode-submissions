class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1] * (len(nums) + 1)
        suf = [1] * (len(nums) + 1)

        for i in range(1, len(nums)+1):
            pre[i] = nums[i-1] * pre[i-1]
        # print(pre)

        for i in range(len(nums)-1, -1, -1):
            suf[i] = nums[i] * suf[i+1]
        # print(suf)

        ans = []
        for i in range(len(nums)):
            ans.append(pre[i]*suf[i+1])
        
        return ans
