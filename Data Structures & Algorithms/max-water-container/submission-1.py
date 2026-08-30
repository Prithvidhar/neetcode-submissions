class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        j = len(heights) - 1
        i = 0
        while i < j:
            print(i, j)
            result = max(result, (j-i) * min(heights[j], heights[i]))
            if heights[j] > heights[i]:
             i = i + 1
            else:
             j = j - 1
        
        return result
        