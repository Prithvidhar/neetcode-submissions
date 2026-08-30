class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result = result + str(len(s)) + "#" + s
        print(result)
        return result
 
    def decode(self, s: str) -> List[str]:
        j = 0
        i = 0
        print(s)
        result = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j = j +1
            length = int(s[i:j])
            result.append(s[j+1: j+1+length])
            i = j + 1 + length
        return result
