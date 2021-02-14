import sys
from collections import defaultdict
from math import gcd

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def make_divisors(n):
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return divisors


def solve():
    _ = int(rl())
    A = list(map(int, rl().split()))
    
    d = defaultdict(int)
    for ai in A:
        divs = make_divisors(ai)
        for div in divs:
            d[div] = gcd(d[div], ai)

    min_A = min(A)
    ans = sum(min_A >= val == key for key, val in d.items())
    print(ans)


if __name__ == '__main__':
    solve()
