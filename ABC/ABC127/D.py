from operator import itemgetter


def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    BC = [[] for _ in range(M)]
    for i in range(M):
        BC[i] = list(map(int, input().split()))
    BC.sort(key=itemgetter(1), reverse=True)
    
    change = []
    for b, c in BC:
        change += [c for _ in range(b)]
        if N < len(change):
            break
    
    A += change
    A.sort()
    ans = sum(A[:-N])
    print(ans)


if __name__ == '__main__':
    solve()
