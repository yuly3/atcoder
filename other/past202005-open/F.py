import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    a = [rl().rstrip() for _ in range(N)]
    
    ans = [''] * N
    for t in range((N + 1) // 2):
        d = N - t - 1
        can_use = set(a[t]) & set(a[d])
        if not can_use:
            print(-1)
            return
        for si in can_use:
            ans[t] = si
            ans[d] = si
            break
    print(''.join(ans))


if __name__ == '__main__':
    solve()
