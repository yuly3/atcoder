import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    A = list(map(int, rl().split()))
    B = list(map(int, rl().split()))
    
    ma = max(A)
    mb = min(B)
    ans = mb - ma + 1
    print(ans if 0 <= ans else 0)


if __name__ == '__main__':
    solve()
