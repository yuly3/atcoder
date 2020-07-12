import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    a = list(map(int, rl().split()))
    
    ans = 0
    for i in range(0, N, 2):
        if i % 2 == 0 and a[i] % 2 == 1:
            ans += 1
    print(ans)


if __name__ == '__main__':
    solve()
