class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        county = defaultdict(int)
        for i in nums:
            if county[i] >1:
                return True
            elif i in county:
                county[i] = county[i] + 1
            else:
                county[i] = 1
            if county[i] > 1:return True
        return False
        
        