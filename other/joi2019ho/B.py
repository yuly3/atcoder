import sys
from operator import itemgetter

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, M = map(int, rl().split())
    SV = [tuple(map(int, rl().split())) for _ in range(N)]
    C = [int(rl()) for _ in range(M)]
    
    SV.sort(key=itemgetter(1, 0), reverse=True)
    C.sort(reverse=True)
    
    ans = 0
    for i in range(N):
        if ans == M:
            break
        if SV[i][0] <= C[ans]:
            ans += 1
    print(ans)


if __name__ == '__main__':
    solve()
