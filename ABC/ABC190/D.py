import sys

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
    N = int(rl())
    
    N *= 2
    divs = make_divisors(N)
    ans = 1
    for div in divs:
        if div == N:
            continue
        d = N // div
        ans += div % 2 == 0 and d % 2 == 1 or div % 2 == 1 and d % 2 == 0
    print(ans)


if __name__ == '__main__':
    solve()
