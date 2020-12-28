import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    H, W = map(int, rl().split())
    A = [list(map(int, rl().split())) for _ in range(H)]
    
    c = min(min(ai) for ai in A)
    ans = sum(sum(aij - c for aij in ai) for ai in A)
    print(ans)


if __name__ == '__main__':
    solve()
