import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    X, N = map(int, rl().split())
    p = set(map(int, rl().split()))
    
    ans = -1
    d_min = 1000
    for i in range(102):
        if i not in p:
            if abs(X - i) < d_min:
                d_min = abs(X - i)
                ans = i
    print(ans)


if __name__ == '__main__':
    solve()
