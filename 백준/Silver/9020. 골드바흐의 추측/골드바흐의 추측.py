import sys
import math

a = int(input())
arr = list(map(int, sys.stdin.read().split()))

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    limit = math.isqrt(n)
    for i in range(3, limit + 1, 2): # 3부터 limit 까지, 증가폭은 2(홀수만 봐야 하니까)
        if n % i == 0:
            return False
    return True

for i in arr:
    tmp = i // 2

    for j in range(tmp, 0, -1):
        if is_prime(j) == True:
            if is_prime(i - j) == True:
                print(f"{j} {i - j}")
                break