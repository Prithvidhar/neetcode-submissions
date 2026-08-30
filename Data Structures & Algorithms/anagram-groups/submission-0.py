class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashy = defaultdict(list)
        for s in strs:
            hashy[tuple(sorted(s))].append(s)
        print(hashy)
        return list(hashy.values())

