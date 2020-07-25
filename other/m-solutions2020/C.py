import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, K = map(int, rl().split())
    A = list(map(int, rl().split()))
    
    l_i = 0
    ans = []
    for ai in A[K:]:
        ans.append('Yes' if A[l_i] < ai else 'No')
        l_i += 1
    print(*ans, sep='\n')


if __name__ == '__main__':
    solve()
