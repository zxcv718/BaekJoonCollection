import sys
input = sys.stdin.readline

n = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(n)]

# 핵심: 종료시간 오름차순, 같으면 시작시간 오름차순
meetings.sort(key=lambda x: (x[1], x[0]))

cnt = 0
last_end = -10**18  # 직전 선택 회의 종료시각
for s, e in meetings:
    if s >= last_end:   # 끝나자마자 시작 허용
        cnt += 1
        last_end = e

print(cnt)
