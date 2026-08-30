import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-n for n in nums]
        heapq.heapify(nums)

        for i in range(1,k):
            heapq.heappop(nums)
        return -heapq.heappop(nums)
        