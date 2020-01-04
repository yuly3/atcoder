from collections import defaultdict


def solve():
    N, *A = map(int, open(0).read().split())
    
    ans, l = 0, 0
    dict = defaultdict(int)
    for r in range(N):
        while l <= r:
            if A[r] not in dict:
                ans = max(ans, r - l + 1)
                dict[A[r]] = 1
                break
            else:
                del dict[A[l]]
                l += 1
    print(ans)


if __name__ == '__main__':
    solve()
