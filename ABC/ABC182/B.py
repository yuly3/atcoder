import sys
from collections import Counter

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
    
    counter = Counter()
    for ai in A:
        divs = make_divisors(ai)
        for div in divs:
            if div == 1:
                continue
            counter[div] += 1
    print(max(counter, key=counter.get))


if __name__ == '__main__':
    solve()
