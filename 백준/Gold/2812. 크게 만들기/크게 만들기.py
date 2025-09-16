n, k = map(int, input().split())
num = input().strip() # 앞뒤 공백 제거

stack = []

for i in num:
    while k > 0 and stack and stack[-1] < i:
        stack.pop()
        k -= 1
    stack.append(i)

if k > 0:
    for _ in range(k):
        stack.pop()
print(*stack, sep='')