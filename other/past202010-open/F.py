import sys
from collections import Counter
from operator import itemgetter

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, K = map(int, rl().split())
    S = [rl().rstrip() for _ in range(N)]
    
    counter = Counter(S)
    T = [(val, key) for key, val in counter.items()]
    T.sort(key=itemgetter(0), reverse=True)
    
    N = len(T)
    if N == 1:
        print(S[0])
        return
    
    K -= 1
    if K == 0 and T[K][0] == T[K + 1][0] or K == N - 1 and T[K][0] == T[K - 1][0]:
        print('AMBIGUOUS')
        return
    if K != 0 and K != N - 1 and (T[K - 1][0] == T[K][0] or T[K + 1][0] == T[K][0]):
        print('AMBIGUOUS')
        return
    
    print(T[K][1])


if __name__ == '__main__':
    solve()
