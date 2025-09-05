import math
a, b, c = map(int, input().split())

if a == c:
    print(1)
else:
    print(math.ceil((c - a) / (a - b) + 1))
