import sys

input = sys.stdin.readline

n = int(input())

def tile(n):
    if n < 3:
        return n
    else:
        a = 1
        b = 2
        for _ in range(3, n + 1):
            temp = a
            a = b
            b = (temp + b) % 15746
        return b

print(tile(n))
