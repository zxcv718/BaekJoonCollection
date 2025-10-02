import sys
input = sys.stdin.readline

n = int(input())

if n == 1 or n == 3:
    print(-1)
    sys.exit(0)
if n % 2 == 0:
    f = n // 10
    s = (n % 10) // 2
    print(f * 2 + s)
    sys.exit(0)
else:
    f = n // 10
    s = (n % 10 - 5) // 2
    if (n % 10 - 5) < 0:
        f -= 1
        s = (n % 10 + 5) // 2
    print(f * 2 + 1 + s)
    sys.exit(0)