import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, M = map(int, rl().split())
    H = list(map(int, rl().split()))
    graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(lambda x: int(x) - 1, rl().split())
        graph[a].append(b)
        graph[b].append(a)
    
    ans = 0
    for i in range(N):
        flg = True
        for child in graph[i]:
            if H[i] <= H[child]:
                flg = False
        ans += flg
    print(ans)


if __name__ == '__main__':
    solve()
