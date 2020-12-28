import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    A = list(map(int, rl().split()))
    
    A.sort()
    ans = 0
    for i, ai in enumerate(A):
        ans -= ai * (N - i - 1)
        ans += ai * i
    print(ans)


if __name__ == '__main__':
    solve()
