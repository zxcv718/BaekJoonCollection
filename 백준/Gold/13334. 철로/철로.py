import heapq

n = int(input())
pairs = [tuple(map(int, input().split())) for _ in range(n)]
pairs = [(min(a,b), max(a,b)) for a,b in pairs]
pairs.sort(key=lambda x: x[1])
d = int(input())

heap = []
ans = 0

for i in range(0, len(pairs)):
    heapq.heappush(heap, pairs[i][0])
    while heap and heap[0] < pairs[i][1] - d:
        heapq.heappop(heap)
    ans = max(ans, len(heap))

print(ans)