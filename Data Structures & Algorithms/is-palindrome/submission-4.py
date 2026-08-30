class Solution:
    def isPalindrome(self, s: str) -> bool:
        twop = len(s) - 1
        start = 0
        
        while start < len(s)-1 and twop >= 0:
            print(s[start], s[twop])
            print(start, twop, "before")
            if not s[start].isalnum():
                start = start +1
                continue
            if not s[twop].isalnum():
                twop = twop -1
                continue
            if not s[start].isalnum() and not s[twop].isalnum():
                start = start +1
                twop = twop -1
                continue
            # check char
            print(start, twop, "after")
            # print(s[start], s[twop])
            if  not s[start].lower() == s[twop].lower():
                print(s[start], s[twop])
                return False
            start = start + 1
            twop = twop -1

            
        return True