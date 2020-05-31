import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    _ = int(rl())
    A = list(map(int, rl().split()))
    if any(ai == 0 for ai in A):
        print(0)
        return
    ans = 1
    for ai in A:
        ans *= ai
        if 10 ** 18 < ans:
            print(-1)
            return
    print(ans)


if __name__ == '__main__':
    solve()
