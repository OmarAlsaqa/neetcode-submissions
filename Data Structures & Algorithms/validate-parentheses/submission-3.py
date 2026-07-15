class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
            
        stack = []
        for i in s:
            if i in "({[":
                stack.append(i)
            else:
                if not stack or not (0 < ord(i) - ord(stack.pop()) <= 2):
                    return False
                    
        return not stack