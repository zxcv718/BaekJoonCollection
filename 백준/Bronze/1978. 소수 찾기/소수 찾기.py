import math

a = int(input())
arr = list(map(int, input().split()))
count = 0

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
    if is_prime(i) == True:
        count += 1
        
print(count)
        
