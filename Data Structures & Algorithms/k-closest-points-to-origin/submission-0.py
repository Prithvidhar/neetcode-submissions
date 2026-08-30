import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Getting disonacne
        print(points)
        distances = []
        for p in range(len(points)):
            distances.append((points[p][0]**2 + points[p][1]**2,points[p]))

        print("distances")
        print(distances)
        heapq.heapify(distances)
        ans = []
        for i in range(k):
            print("ans")
            ans.append(heapq.heappop(distances)[1])
        print(ans)
        return ans
            

        