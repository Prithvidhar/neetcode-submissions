class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        for i in range(len(heights)):
            j = i + 1
            while j < len(heights):
                height = min(heights[i],heights[j])
                width = j - i
                result  = max(result, height * width)
                j = j + 1
        return result
        