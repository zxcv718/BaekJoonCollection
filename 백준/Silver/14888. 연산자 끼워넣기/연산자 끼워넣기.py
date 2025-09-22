import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n = int(input().strip())
operands = list(map(int, input().split()))
operators = list(map(int, input().split()))

def calculate(op, rand1, rand2):
    if op == 0:
        return rand1 + rand2
    elif op == 1:
        return rand1 - rand2        
    elif op == 2:
        return rand1 * rand2
    elif op == 3:
        if rand1 < 0:
            return -(-rand1 // rand2)
        else:
            return rand1 // rand2

maxv = -1000000000
minv = 1000000000

def dfs(i, num):
    global maxv, minv

    if i == n:
        maxv = max(maxv, num)
        minv = min(minv, num)
        return

    for op in range(4):
        if operators[op] == 0:
            continue
        operators[op] -= 1
        temp = calculate(op, num, operands[i])
        dfs(i + 1, temp)
        operators[op] += 1

dfs(1, operands[0])
print(maxv)
print(minv)