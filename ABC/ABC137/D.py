import sys
import heapq

input = sys.stdin.readline


def solve():
    N, M = map(int, input().split())
    jobs = [[] for _ in range(M)]
    for i in range(N):
        a, b = map(int, input().split())
        if a - 1 < M:
            jobs[a - 1].append(-b)

    ans = 0
    hq = []
    for i in range(M):
        for job in jobs[i]:
            heapq.heappush(hq, job)
        if len(hq) > 0:
            ans += -heapq.heappop(hq)

    print(ans)


if __name__ == '__main__':
    solve()
