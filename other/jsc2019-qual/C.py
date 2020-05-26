import sys
from math import factorial

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline
MOD = 10 ** 9 + 7


def solve():
    N = int(rl())
    S = rl().rstrip()
    
    if S[0] == 'W' or S[-1] == 'W':
        print(0)
        return
    
    flip = [0] * (2 * N)
    cntl, cntr = 1, 0
    ans = 1
    for i in range(1, 2 * N):
        if S[i] == S[i - 1]:
            flip[i] = flip[i - 1] ^ 1
        else:
            flip[i] = flip[i - 1]
        if flip[i] == 0:
            cntl += 1
        else:
            ans = ans * (cntl - cntr) % MOD
            cntr += 1
    
    if cntl != cntr:
        print(0)
    else:
        ans = ans * factorial(N) % MOD
        print(ans)


if __name__ == '__main__':
    solve()
