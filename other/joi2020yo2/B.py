import sys
from operator import itemgetter

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    AT = [list(map(int, rl().split())) for _ in range(N)]
    AT.sort(key=itemgetter(0))
    A, T = [], []
    for ai, ti in AT:
        A.append(ai)
        T.append(ti)
    
    ans = max(A[-1], T[-1])
    for i in range(N - 2, -1, -1):
        ans = max(ans + A[i + 1] - A[i], T[i])
    ans += A[0]
    print(ans)


if __name__ == '__main__':
    solve()
