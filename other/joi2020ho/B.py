import sys
from bisect import bisect_left

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, K = map(int, rl().split())
    S = rl().rstrip()
    
    posj, poso, posi = [], [], []
    for i in range(N):
        if S[i] == 'J':
            posj.append(i)
        elif S[i] == 'O':
            poso.append(i)
        else:
            posi.append(i)
    
    ans = 10 ** 7
    for i in range(len(posj) - K + 1):
        s = posj[i]
        cur = posj[i + K - 1]
        idx = bisect_left(poso, cur)
        if len(poso) <= idx + K - 1:
            break
        cur = poso[idx + K - 1]
        idx = bisect_left(posi, cur)
        if len(posi) <= idx + K - 1:
            break
        t = posi[idx + K - 1]
        ans = min(ans, (t - s + 1) - 3 * K)
    
    print(ans if ans != 10 ** 7 else -1)


if __name__ == '__main__':
    solve()
