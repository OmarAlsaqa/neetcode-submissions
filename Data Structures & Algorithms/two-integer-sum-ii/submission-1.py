class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s, n = 0, len(numbers)-1
        
        while n > s:
            v1 = numbers[s]
            v2 = numbers[n]

            if v1 + v2 == target:
                return [s+1, n+1]
            
            elif v1 + v2 > target:
                n -= 1
            
            elif v1 + v2 < target:
                s += 1