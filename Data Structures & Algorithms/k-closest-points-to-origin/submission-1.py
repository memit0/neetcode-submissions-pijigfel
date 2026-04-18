class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []
        for x, y in points:
            dist = math.sqrt((x - 0)**2 + (y - 0)**2)
            # python pushes and pops into a heap based on the first val of tuple
            heapq.heappush(heap, (dist, [x, y]))

        for i in range(k):
            dist, coord = heapq.heappop(heap)
            res.append(coord)

        return res

