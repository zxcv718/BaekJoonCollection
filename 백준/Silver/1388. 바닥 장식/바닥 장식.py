import sys

input = sys.stdin.readline

n, m = map(int, input().split())

floor = [[] * m for _ in range(n)]

for i in range(n):
    floor[i] = list(input().strip())

v = 0
h = 0


for i in range(n):
    prev = ''
    for j in range(m):
        if floor[i][j] == '-':
            if floor[i][j] != prev:
                h += 1
        prev = floor[i][j]

for j in range(m):
    prev = ''
    for i in range(n):
        if floor[i][j] == '|':
            if floor[i][j] != prev:
                v += 1
        prev = floor[i][j]

print(h + v)