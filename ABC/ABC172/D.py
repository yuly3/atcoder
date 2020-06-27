import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    
    ans = 0
    for i in range(1, N + 1):
        j = N // i
        ans += j * (j + 1) * i // 2
    print(ans)


if __name__ == '__main__':
    solve()
