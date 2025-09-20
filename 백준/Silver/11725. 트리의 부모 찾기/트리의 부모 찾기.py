import sys

input = sys.stdin.readline

n = int(input().strip())
adj = [[] for _ in range(n + 1)]
p = [0] * (n + 1)

for _ in range(n - 1):
    a, b = map(int, input().strip().split())
    adj[a].append(b)
    adj[b].append(a)
#BFS, 어차피 모든 노드 다 방문이라 방문체크 불필요, 부모체크라 같은 레벨에 있는 노드들을 다 순회하는 BFS가 적절
def bfs(root):
    q = [root]
    cur = 0
    while cur < len(q):
        u = q[cur]
        cur += 1
        for v in adj[u]:
            if p[v] == 0 and v != 1:# 핵심 조건
                p[v] = u                
                q.append(v)

bfs(1)
print(*p[2:], sep="\n")