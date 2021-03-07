import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    A = list(map(int, rl().split()))
    
    su = sum(A)
    ans = 0
    for i, ai in enumerate(A):
        ans += (N - 1) * ai ** 2
        su -= ai
        ans += -2 * ai * su
    print(ans)


if __name__ == '__main__':
    solve()
