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
    
    divs = sorted(make_divisors(N))
    print('\n'.join(map(str, divs)))


if __name__ == '__main__':
    solve()
