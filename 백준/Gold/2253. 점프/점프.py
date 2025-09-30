import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
small = set()

for _ in range(m):
    s = int(input())
    small.add(s)

q = deque()
dist = {(1, 0): 0}
q.append((1, 0))
candidate = [-1, 0, 1]

def bfs():
    while q:
        s, prev = q.popleft()
        
        if s == n:
            print(dist[(s, prev)])
            return
        
        for i in candidate:
            next = prev + i
            
            if next <= 0:
                continue

            nStone = s + next
            
            if nStone > n:
                break
            
            if nStone not in small:
                if (nStone, next) not in dist:
                    dist[(nStone, next)] = dist[(s, prev)] + 1
                    q.append((nStone, next))
    
    print(-1)

bfs()