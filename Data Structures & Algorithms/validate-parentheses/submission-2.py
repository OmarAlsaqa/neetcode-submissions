class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) % 2 != 0:
            return False
        for i in s:
            if i == "{" or i == "(" or i == "[":
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                ord_ = ord(i) - ord(stack[-1])
                if ( ord_ <= 2) and (ord_ > 0):
                    l = stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
