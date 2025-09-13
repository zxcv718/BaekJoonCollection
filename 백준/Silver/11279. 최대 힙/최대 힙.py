import heapq
import sys

n = int(input())
nums = list(map(int, sys.stdin.read().split()))
heap = []

for i in nums:
    if i == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(-heapq.heappop(heap))
    else:
        heapq.heappush(heap, -i)