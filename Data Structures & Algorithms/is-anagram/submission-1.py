class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        county = defaultdict(int)
        for i in s:
            if i in county:
                county[i] = county[i] + 1
            else:
                county[i] = 1
        for j in t:
            if j not in county:
                return False
            else:
                county[j] = county[j] +1
        for k in county:
            if county[k] %2 != 0:
                return False
        return True
        