import sys
from collections import deque
input = sys.stdin.readline
#kahn 알고리즘
n, m = map(int, input().split())
arr = [[] for _ in range(n + 1)]
lev = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())   # a가 b보다 앞(간선 a->b)
    arr[a].append(b)                   
    lev[b] += 1                  # append가 되었다는건 진입차수가 0이 아님    

q = deque([i for i in range(1, n + 1) if lev[i] == 0])  # 시작점: 진입차수 0
ans = []

while q:
    u = q.popleft()
    ans.append(u)
    for v in arr[u]:
        lev[v] -= 1 # 이 시점에 모든 v는 최소한 차수가 1 이상, 그렇지 않으면 여기에 진입 불가
        if lev[v] == 0:
            q.append(v)

print(*ans)
