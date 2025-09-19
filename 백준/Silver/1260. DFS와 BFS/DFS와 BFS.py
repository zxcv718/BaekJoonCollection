import sys
from collections import deque
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n, m, start = map(int, input().split())
adj = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().strip().split())
    adj[a].append(b)
    adj[b].append(a)

for neighbors in adj:
    neighbors.sort()

d_visited = [False] * (n + 1)
b_visited = [False] * (n + 1)

d_ans = []
b_ans = []

def dfs(s):
    d_visited[s] = True
    d_ans.append(s)
    for v in adj[s]:
        if not d_visited[v]:
            dfs(v)

def bfs(s):
    q = deque([s])
    b_visited[s] = True
    b_ans.append(s) 
    while q:
        u = q.popleft()
        for v in adj[u]:
            if not b_visited[v]:
                b_visited[v] = True
                b_ans.append(v) # 재귀가 아니기 때문에 append를 추가로 해야함
                q.append(v)

dfs(start)
bfs(start)

print(*d_ans)
print(*b_ans)