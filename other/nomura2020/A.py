import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    H1, M1, H2, M2, K = map(int, rl().split())
    
    t1 = H1 * 60 + M1
    t2 = H2 * 60 + M2
    ans = t2 - K - t1
    print(ans)


if __name__ == '__main__':
    solve()
