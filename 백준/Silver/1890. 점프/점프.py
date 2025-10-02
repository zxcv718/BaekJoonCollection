import sys

input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

ways = [[0] * n for _ in range(n)]
ways[0][0] = 1

for i in range(n):
    for j in range(n):
        if ways[i][j] == 0 or board[i][j] == 0:
            continue

        jump = board[i][j]
        down = i + jump
        right = j + jump

        if down < n:
            ways[down][j] += ways[i][j]
        if right < n:
            ways[i][right] += ways[i][j]

print(ways[n - 1][n - 1])