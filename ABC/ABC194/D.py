import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    
    ans = 0
    for i in range(1, N):
        ans += N / (N - i)
    print(ans)


if __name__ == '__main__':
    solve()
