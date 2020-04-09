import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, P = map(int, rl().split())
    S = input()
    
    ans = 0
    if P == 2 or P == 5:
        for i in range(N - 1, -1, -1):
            si = int(S[i])
            if si % P == 0:
                ans += i + 1
    else:
        cum = [0]
        t = 1
        for i in range(N - 1, -1, -1):
            cum.append(int(S[i]) * t % P)
            t = t * 10 % P
        for i in range(N):
            cum[i + 1] = (cum[i + 1] + cum[i]) % P
        
        counter = defaultdict(int)
        for val in cum:
            ans += counter[val]
            counter[val] += 1
    print(ans)


if __name__ == '__main__':
    solve()
