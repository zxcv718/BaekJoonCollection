import sys

input = sys.stdin.readline

n, m = map(int, input().split())
small = set()

for _ in range(m):
    s = int(input())
    small.add(s)

inf = float('inf')
max_v = int((2 * n) ** 0.5) + 2  # 최대 속도

# dp[i][j] = i번째 돌에 속도 j로 도착하는 최소 점프 횟수
dp = [[inf] * max_v for _ in range(n + 1)]
dp[1][0] = 0

for i in range(2, n + 1):
    if i in small:  # 작은 돌은 건너뛰기
        continue
    
    for j in range(1, int((2 * i) ** 0.5) + 2):  # 가능한 속도 범위
        # i-j 위치에서 속도 j-1, j, j+1로 도착했을 때
        if i - j >= 1:
            dp[i][j] = min(
                dp[i-j][j-1] if j-1 >= 0 else inf,
                dp[i-j][j],
                dp[i-j][j+1] if j+1 < max_v else inf
            ) + 1

answer = min(dp[n])
print(answer if answer != inf else -1)
