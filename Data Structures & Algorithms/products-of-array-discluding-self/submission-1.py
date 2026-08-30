class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        b = 1
        for i in range(len(nums)):
            j = 0
            b = 1
            while j < len(nums):
                if j != i:
                    b = b * nums[j]
                j = j +1
            result.append(b)
        return result
        

        