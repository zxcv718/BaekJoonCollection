string = input().strip()
exp_str = input().strip()

stack = []
for char in string:
    exp_len = len(exp_str)
    stack.append(char)
    if len(stack) >= exp_len and ''.join(stack[-exp_len:]) == exp_str:
        del stack[-exp_len:]

if stack:
    print(''.join(stack))
else:
    print("FRULA")