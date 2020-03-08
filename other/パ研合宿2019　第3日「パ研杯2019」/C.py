from itertools import combinations


def solve():
    N, M = map(int, input().split())
    A = [[] for _ in range(N)]
    for i in range(N):
        A[i] = list(map(int, input().split()))
    
    ans = 0
    for t1, t2 in combinations(range(M), 2):
        p = 0
        for i in range(N):
            p += max(A[i][t1], A[i][t2])
        ans = max(ans, p)
    print(ans)


if __name__ == '__main__':
    solve()
