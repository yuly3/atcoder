import sys
from collections import Counter

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    A = list(map(int, rl().split()))
    MOD = 10 ** 9 + 7
    
    counter = Counter(A)
    if N % 2 == 0:
        for n in range(1, N, 2):
            if counter[n] != 2:
                print(0)
                return
    else:
        if counter[0] != 1:
            print(0)
            return
        for n in range(2, N, 2):
            if counter[n] != 2:
                print(0)
                return
    print(pow(2, N // 2, MOD))


if __name__ == '__main__':
    solve()
