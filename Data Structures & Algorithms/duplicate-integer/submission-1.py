class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setty = set(nums)
        if len(setty) != len(nums): return True
        return False