n = int(input())
arr = list(map(int, input().split()))

# 원 배열의 순서를 변경하지 않는다
# 가능한 길이의 최대치를 찾는다, 예를 들어 원래 2,5 였다가 2보다는 크고 5보다는 작은 값을 찾았으면 마지막 5를 작은 값으로 바꾼다. 최장길이 가능성 증가를 위해
def lower_bound(t, x):
    lo, hi = 0, len(t)      # [lo, hi)
    while lo < hi:
        mid = (lo + hi) // 2
        if t[mid] < x:      # 엄격 증가(LIS) → x와 같으면 자리 유지해야 하므로 '<' 사용
            lo = mid + 1
        else:
            hi = mid
    return lo

tails = []
for x in arr:                 # 입력 순서 그대로 처리
    i = lower_bound(tails, x)
    if i == len(tails):
        tails.append(x)     # 길이 1 증가
    else:
        tails[i] = x        # 해당 길이의 꼬리값 최소화

print(len(tails))