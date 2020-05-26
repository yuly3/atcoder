import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    S = rl().rstrip()
    
    accw, acce = [0] * (N + 1), [0] * (N + 1)
    for i in range(N):
        accw[i + 1] = accw[i] + (S[i] == 'W')
        acce[i + 1] = acce[i] + (S[i] == 'E')
    
    ans = 10 ** 6
    for i in range(N):
        ans = min(ans, acce[-1] - acce[i + 1] + accw[i])
    print(ans)


if __name__ == '__main__':
    solve()
