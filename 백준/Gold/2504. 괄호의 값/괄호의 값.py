s = input()

def solve(s: str) -> int:
    stack = []
    mul = 1
    ans = 0
    weight = {'(': 2, '[': 3}
    pairs = {')': '(', ']': '['}
    prev = ''

    for ch in s:
        if ch == '(' or ch == '[':
            stack.append(ch)
            mul *= weight[ch]
        elif ch == ')' or ch == ']':
            # 1) 짝 검증 (스택 비었거나 top 불일치면 0)
            if not stack or stack[-1] != pairs[ch]:
                return 0
            # 2) 즉시쌍일 때만 가산
            if prev == pairs[ch]:
                ans += mul
            # 3) 닫았으니 배율 복원 + pop
            stack.pop()
            mul //= weight[pairs[ch]]
        else:
            return 0  # 문제 도메인 외 문자 방어
        prev = ch
    # 4) 모두 처리 후 스택 비어야 올바름
    return ans if not stack else 0

print(solve(s))