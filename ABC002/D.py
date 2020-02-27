from itertools import combinations


def solve():
    N, M = map(int, input().split())
    xy = set()
    for _ in range(M):
        x, y = map(int, input().split())
        xy.add((x, y))
    
    ans = 0
    for i in range(N, 0, -1):
        for members in combinations(range(1, N+1), i):
            for comb in combinations(members, 2):
                if comb not in xy:
                    break
            else:
                ans = max(ans, i)
                break
    print(ans)


if __name__ == '__main__':
    solve()
