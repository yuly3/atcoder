import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    
    se = set()
    for a in range(2, int(N ** 0.5) + 2):
        n = a ** 2
        while n <= N:
            se.add(n)
            n *= a
    print(N - len(se))


if __name__ == '__main__':
    solve()
