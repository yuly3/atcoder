import sys
from itertools import accumulate

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    A = list(map(int, rl().split()))
    
    acc_a = list(accumulate(A))
    max_move = [0] * N
    if 0 < A[0]:
        max_move[0] = A[0]
    for i in range(1, N):
        max_move[i] = max(max_move[i - 1], acc_a[i])
    
    ans = 0
    pos = 0
    for i in range(N):
        ans = max(ans, pos + max_move[i])
        pos += acc_a[i]
    print(ans)


if __name__ == '__main__':
    solve()
