a = int(input()) # 첫 번째 숫자 입력
b = int(input()) # 두 번째 숫자 입력

for i in str(b)[::-1]: # b의 각 자리 숫자를 역순으로 접근
    print(a * int(i)) # 각 자리 숫자와 a의 곱 출력
print(a * b) # a와 b의 곱 출력