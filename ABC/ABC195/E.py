import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    S = rl().rstrip()
    X = rl().rstrip()
    
    dp = [[] for _ in range(N + 1)]
    dp[N].append(0)
    for i in range(N, 0, -1):
        si = int(S[i - 1])
        if X[i - 1] == 'T':
            for j in range(7):
                if 10 * j % 7 in dp[i] or (10 * j + si) % 7 in dp[i]:
                    dp[i - 1].append(j)
        else:
            for j in range(7):
                if 10 * j % 7 in dp[i] and (10 * j + si) % 7 in dp[i]:
                    dp[i - 1].append(j)
    print('Takahashi' if 0 in dp[0] else 'Aoki')


if __name__ == '__main__':
    solve()
