import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    _ = int(rl())
    S = rl().rstrip()
    
    ans = ''
    for i, si in enumerate(S):
        if si in S[i + 1:]:
            continue
        ans += si
    print(ans)


if __name__ == '__main__':
    solve()
