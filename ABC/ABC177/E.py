import sys
from functools import reduce
from math import gcd

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def eratosthenes(n):
    prime = [2]
    if n == 2:
        return prime
    limit = int(n ** 0.5)
    data = [i + 1 for i in range(2, n, 2)]
    res = [0] * (n + 1)
    res[1] = 1
    for i in range(2, n + 1, 2):
        res[i] = 2
    while True:
        p = data[0]
        if limit <= p:
            for e in data:
                res[e] = e
            return res
        prime.append(p)
        res[p] = p
        for e in data:
            if e % p == 0:
                res[e] = p
        data = [e for e in data if e % p != 0]


def solve():
    _ = int(rl())
    A = list(map(int, rl().split()))
    
    prime_fact = eratosthenes(10 ** 6)
    p_flg = True
    prime_fact_set = set()
    for ai in A:
        num = ai
        prime_fact_ai = set()
        while num != 1:
            prime_fact_ai.add(prime_fact[num])
            num //= prime_fact[num]
        for p in prime_fact_ai:
            if p in prime_fact_set:
                p_flg = False
                break
            prime_fact_set.add(p)
        if not p_flg:
            break
    
    if p_flg:
        print('pairwise coprime')
        return
    
    gcd_a = reduce(gcd, A)
    if gcd_a == 1:
        print('setwise coprime')
        return
    
    print('not coprime')


if __name__ == '__main__':
    solve()
