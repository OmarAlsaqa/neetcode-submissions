class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = 999
        maxi = -999
        max_diff = 0
        for i in prices:
            if i < mini:
                mini = i
                maxi = -999
            if i > maxi:
                maxi = i
                diff = maxi - mini
                if diff > max_diff:
                    max_diff = diff
        return max_diff
