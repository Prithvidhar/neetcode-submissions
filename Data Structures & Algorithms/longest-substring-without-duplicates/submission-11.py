class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 1
        maxi = 0
        
        if len(s) == 1:
            return 1
        if len(s) == 0:
            return 0
        setty = set(s[start])
        while start < len(s):
            print(start,end)
            if s[end] in setty:
                # print("equals!",s[start:end], maxi)
                print("equals!",setty)
                maxi = max(len(setty), maxi)
                setty = set(s[start])
                start = start+1
                end = start
                
            else:
                setty.add(s[end])
                end = end + 1
            if end == len(s):
                
                maxi = max(len(setty), maxi)
                print("end",setty, s[start:end])
                
                # print("end", s[start:end] )
                start = start +1
                end = min(len(s)-1,start + 1)
                print(maxi)
                
                
                
        print("post",setty, maxi)
        if maxi == 0: return len(s)
        return max(len(setty), maxi)
        