class Solution:
    def isPalindrome(self, s: str) -> bool:
        for ind, i in enumerate(s):
            print(i)
            if i == " ":
                continue
            elif (ord(i) <= ord('z')) and (ord(i) >= ord('a')):
                continue
            elif (ord(i) <= ord('Z')) and (ord(i) >= ord('A')):
                continue
            elif (ord(i) <= ord('9')) and (ord(i) >= ord('0')):
                continue
            else:
                s = s.replace(s[ind], " ")
            print(s[ind])
        
        s = "".join(s.split(" ")).lower()
        print(s)

        if s == "" or s == " ":
            return True

        for i in range(len(s)//2+1):
            print(i, s[i], s[len(s)-1-i])
            if s[i] == s[len(s)-1-i]:
                continue
            else:
                return False

        return True


