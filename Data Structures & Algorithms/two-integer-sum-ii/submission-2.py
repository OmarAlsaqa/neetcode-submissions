class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s, n = 0, len(numbers)-1
        
        while n > s:
            psum = numbers[s] + numbers[n]

            if psum == target:
                return [s+1, n+1]
            
            elif psum > target:
                n -= 1
            
            elif psum < target:
                s += 1