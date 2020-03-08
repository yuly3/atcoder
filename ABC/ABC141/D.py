import heapq as hq


def solve():
    N, M = map(int, input().split())
    pl = list(map(lambda x: int(x) * (-1), input().split()))
    hq.heapify(pl)

    for _ in range(M):
        tmp = hq.heappop(pl)
        hq.heappush(pl, (-1) * (-tmp // 2))

    print(-sum(pl))


if __name__ == '__main__':
    solve()
