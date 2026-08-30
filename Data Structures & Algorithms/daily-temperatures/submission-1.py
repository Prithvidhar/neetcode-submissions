class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        start = 0
        index = start
        result = []
        while start < len(temperatures):
            index = start + 1
            day = 1
            while index < len(temperatures) and temperatures[index] <= temperatures[start]:
                day = day + 1
                index = index + 1
            if index == len(temperatures) and temperatures[start] >= temperatures[index-1]:
                result.append(0)
            else:
                result.append(day)
            start = start + 1
        return result
        