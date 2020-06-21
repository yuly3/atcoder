import sys
from collections import Counter

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    _ = int(rl())
    A = list(map(int, rl().split()))
    Q = int(rl())
    B, C = [0] * Q, [0] * Q
    for i in range(Q):
        B[i], C[i] = map(int, rl().split())
    
    counter = Counter(A)
    sum_a = sum(A)
    ans = []
    for b, c in zip(B, C):
        sum_a -= counter[b] * b
        sum_a += counter[b] * c
        counter[c] += counter[b]
        counter[b] = 0
        ans.append(sum_a)
    print(*ans, sep='\n')


if __name__ == '__main__':
    solve()
