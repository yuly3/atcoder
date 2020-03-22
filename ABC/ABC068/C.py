import sys
rl = sys.stdin.buffer.readline


def solve():
    N, M = map(int, rl().split())
    graph = [set() for _ in range(N)]
    for _ in range(M):
        a, b = map(lambda x: int(x) - 1, rl().split())
        graph[a].add(b)
        graph[b].add(a)
    
    for child in graph[0]:
        if N - 1 in graph[child]:
            print('POSSIBLE')
            exit()
    print('IMPOSSIBLE')


if __name__ == '__main__':
    solve()
