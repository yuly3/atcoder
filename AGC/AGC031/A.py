import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    _ = rl()
    S = input()
    MOD = 10 ** 9 + 7
    
    counter = defaultdict(int)
    for si in S:
        counter[si] += 1
    
    ans = 1
    s = set(S)
    for si in s:
        ans = ans * (counter[si] + 1) % MOD
    ans -= 1
    print(ans)


if __name__ == '__main__':
    solve()
