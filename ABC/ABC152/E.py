import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])
    
    if temp != 1:
        arr.append([temp, 1])
    if not arr:
        arr.append([n, 1])
    
    return arr


def mod_div(x, y, mod=10 ** 9 + 7):
    return x * pow(y, mod - 2, mod) % mod


def solve():
    _ = int(rl())
    A = list(map(int, rl().split()))
    MOD = 10 ** 9 + 7
    
    max_exp = defaultdict(int)
    for ai in A:
        facts = factorization(ai)
        for fact, m in facts:
            if max_exp[fact] < m:
                max_exp[fact] = m
    
    lcm = 1
    for num, exp in max_exp.items():
        lcm = lcm * pow(num, exp, MOD) % MOD
    
    ans = sum([mod_div(lcm, ai) for ai in A]) % MOD
    print(ans)


if __name__ == '__main__':
    solve()
