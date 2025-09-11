a = int(input())

if a < 10:
    a *= 10

ans = a

count = 0

while True:
    b = a // 10
    c = a % 10
    
    d = b + c # 새로 만들어진 수
    e = (c * 10) + d % 10
    count += 1

    if e == ans:
        print(count)
        break
    else:
        a = e
