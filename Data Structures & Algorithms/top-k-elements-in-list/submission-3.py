class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countHash = defaultdict(int)
        hash = defaultdict(list)
        count = []
        ans = []
        for i in nums:
            countHash[i] = countHash[i] + 1
        # print("countHash is", countHash)
        for i in countHash:
            hash[countHash[i]].append(i)
            count.append(countHash[i])
        count.sort()
        # print("count is", count)
        # print("hash is", hash)
        for j in sorted(hash.keys(),reverse=True):
            if len(ans) >= k:
                break
            # print(-1-j, hash[count[-1-j]])
            ans.extend(hash[j])

        return ans
        