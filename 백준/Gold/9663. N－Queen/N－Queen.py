import sys

N = int(sys.stdin.readline())

# 같은 열 / ↘ 대각(r+c) / ↙ 대각(r-c+N-1) 사용 여부
used_col = [False] * N
used_d1  = [False] * (2*N - 1)
used_d2  = [False] * (2*N - 1)
# 행과 대각선 2방향만 체크하면 열 체크 필요 없음
ans = 0

def dfs(r: int) -> None:
    global ans
    if r == N:           # 모든 행에 1개씩 성공적으로 배치
        ans += 1
        return

    for c in range(N):
        d1 = r + c               # ↘ 대각 인덱스
        d2 = r - c + (N - 1)     # ↙ 대각 인덱스 (음수 방지 오프셋)
        if not used_col[c] and not used_d1[d1] and not used_d2[d2]:
            # 놓는다 (mark)
            used_col[c] = used_d1[d1] = used_d2[d2] = True
            dfs(r + 1)
            # 되돌리기 (unmark)
            used_col[c] = used_d1[d1] = used_d2[d2] = False

dfs(0)
print(ans)
