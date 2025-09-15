a, b, c = map(int, input().split())

def mod_pow(base, exp, mod):
    base %= mod
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

print(mod_pow(a, b, c))
