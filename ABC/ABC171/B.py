import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, K = map(int, rl().split())
    p = list(map(int, rl().split()))
    
    p.sort()
    ans = sum(p[:K])
    print(ans)


if __name__ == '__main__':
    solve()
