import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    
    ans = 20
    for i in range(1, int(N ** 0.5) + 1):
        if N % i == 0:
            a = str(i)
            b = str(N // i)
            ans = min(ans, max(len(a), len(b)))
    print(ans)


if __name__ == '__main__':
    solve()
