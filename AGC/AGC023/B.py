import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    S = [rl().rstrip() for _ in range(N)]
    
    ans = 0
    for b in range(N):
        flg = True
        for i in range(N):
            ii = (i + b) % N
            for j in range(N):
                jj = (j + b) % N
                if S[i][jj] != S[j][ii]:
                    flg = False
                    break
            if not flg:
                break
        ans += flg
    ans *= N
    print(ans)


if __name__ == '__main__':
    solve()
