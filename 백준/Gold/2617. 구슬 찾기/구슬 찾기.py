import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())

arr = [[] for _ in range(n+1)]
rev = [[] for _ in range(n+1)]

half = n//2 
ans = 0

for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    rev[b].append(a)

def bfs_count(start, graph, limit):
    q = deque([start])
    visited = [False]*(n+1)
    visited[start] = True
    cnt = 0
    while q:
        u = q.popleft()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                cnt += 1
                if cnt > limit:
                    return cnt
                q.append(v)
    return cnt

for i in range(1, n+1):
    if bfs_count(i, arr, half) > half or bfs_count(i, rev, half) > half:
        ans += 1

print(ans)