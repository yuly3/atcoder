import sys
from collections import defaultdict
from math import gcd

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline
MOD = 10 ** 9 + 7


def solve():
    N = int(rl())
    AB = tuple(tuple(map(int, rl().split())) for _ in range(N))
    
    zero_pare = 0
    zero_a, zero_b = 0, 0
    counter = defaultdict(int)
    for a, b in AB:
        if a == b == 0:
            zero_pare += 1
        elif a == 0:
            zero_a += 1
        elif b == 0:
            zero_b += 1
        else:
            cd = gcd(a, b)
            a, b = a // cd, b // cd
            if b < 0:
                a, b = -a, -b
            counter[(a, b)] += 1
    
    ans = pow(2, zero_a, MOD) + pow(2, zero_b, MOD) - 1
    memo = set()
    for a, b in list(counter):
        if (a, b) in memo:
            continue
        pa, pb = -b, a
        if pb < 0:
            pa, pb = -pa, -pb
        memo.add((a, b))
        memo.add((pa, pb))
        ans *= pow(2, counter[(a, b)], MOD) + pow(2, counter[(pa, pb)], MOD) - 1
        ans %= MOD
    
    ans = (ans + zero_pare - 1) % MOD
    print(ans)


if __name__ == '__main__':
    solve()
