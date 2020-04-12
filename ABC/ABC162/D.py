import sys
from itertools import combinations

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    S = input()
    
    acc = [[0] * 3 for _ in range(N + 1)]
    for i in range(1, N + 1):
        acc[i] = acc[i - 1][:]
        if S[i - 1] == 'R':
            acc[i][0] += 1
        elif S[i - 1] == 'G':
            acc[i][1] += 1
        else:
            acc[i][2] += 1
    
    ans = 0
    for i, j in combinations(range(N - 1), 2):
        si, sj = S[i], S[j]
        if si == sj:
            continue
        if 'R' not in [si, sj]:
            ans += acc[N][0] - acc[j][0]
            t = j + j - i
            if t < N:
                ans -= S[t] == 'R'
        elif 'G' not in [si, sj]:
            ans += acc[N][1] - acc[j][1]
            t = j + j - i
            if t < N:
                ans -= S[t] == 'G'
        else:
            ans += acc[N][2] - acc[j][2]
            t = j + j - i
            if t < N:
                ans -= S[t] == 'B'
    print(ans)


if __name__ == '__main__':
    solve()
