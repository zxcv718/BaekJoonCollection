#X로부터 출발하여 도달할 수 있는 도시 중에서, 최단 거리가 K인 모든 도시의 번호를 한 줄에 하나씩 오름차순으로 출력한다.
import sys

input = sys.stdin.readline

n, m, k, x = map(int, input().split())
adj = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)

def bfs(s):
    q = [s]
    cur = 0
    visited[s] = True
    depth = 0
    while cur < len(q):
        level_end = len(q)
        while cur < level_end:
            u = q[cur]; cur += 1
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    q.append(v)
        depth += 1
        if depth == k:
            return sorted(q[level_end:len(q)])
    return []

ans = bfs(x)
print(-1 if not ans else "\n".join(map(str, ans)))
