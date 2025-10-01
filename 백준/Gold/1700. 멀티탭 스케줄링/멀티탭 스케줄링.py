import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))
e = []
ans = 0
rest = deque()
reuse = {}

for i, v in enumerate(arr):
    if n > 0:
        if not e.count(v):
            e.append(v)
            n -= 1
    else:
        rest = deque(arr[i:])
        break

def foundReuse():
    reuse.clear()
    for i, v in enumerate(e):
        if v not in rest:
            return i
        else:
            reuse[v] = rest.index(v)
    return -1

while rest:
    c = rest.popleft()
    if c in e:
        continue
    else:
        res = foundReuse()
        if res == -1:
            max_key = max(reuse, key=reuse.get)
            idx = e.index(max_key)
            e[idx] = c
        else:
            e[res] = c
        ans += 1

print(ans)