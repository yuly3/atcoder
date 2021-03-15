import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    
    ans = 0
    for num in (10 ** 3, 10 ** 6, 10 ** 9, 10 ** 12, 10 ** 15):
        if num <= N:
            ans += N - (num - 1)
    print(ans)


if __name__ == '__main__':
    solve()
