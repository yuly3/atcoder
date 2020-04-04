import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, M = map(int, rl().split())
    A = list(map(int, rl().split()))
    
    A.sort(reverse=True)
    sa = sum(A)
    t = sa / (4 * M)
    flg = True
    for i in range(M):
        if A[i] < t:
            flg = False
            break
    if flg:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    solve()
