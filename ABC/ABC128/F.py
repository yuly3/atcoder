import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    s = list(map(int, rl().split()))
    
    ans = 0
    for c in range(1, N):
        cur = 0
        tmp = 0
        i, j = 0, N - 1
        if (N - 1) % c == 0:
            while i < j:
                cur += s[i] + s[j]
                tmp = max(tmp, cur)
                i += c
                j -= c
        else:
            while i < N - 1 and c < j:
                cur += s[i] + s[j]
                tmp = max(tmp, cur)
                i += c
                j -= c
        ans = max(ans, tmp)
    print(ans)


if __name__ == '__main__':
    solve()
