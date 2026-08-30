class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
         
        #Get count
        countOne = defaultdict(int)
        for s in s1:
            countOne[s] = countOne[s] + 1
        print(countOne)
        countTwo = defaultdict(int)
        
        start = 0
        i = start
        j = i + len(s1)
        while j <= len(s2) and i < len(s2):
            countTwo = defaultdict(int)
            i = start
            j = i + len(s1)
            while i < j:
                countTwo[s2[i]] = countTwo[s2[i]] + 1
                i = i +1
            print(countTwo)
            if countOne == countTwo: return True
            start = start + 1
        return False