string = input().strip()
exp_str = input().strip()

stack = []
for char in string:
    exp_len = len(exp_str)
    stack.append(char)
    if ''.join(stack[-exp_len:]) == exp_str:
        for _ in range(exp_len):
            stack.pop()
if stack:
    print(''.join(stack))
else:
    print("FRULA")
