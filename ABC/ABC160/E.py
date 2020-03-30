import sys
import heapq as hq

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    X, Y, A, B, C = map(int, rl().split())
    p = list(map(int, rl().split()))
    q = list(map(int, rl().split()))
    r = list(map(int, rl().split()))
    
    p.sort(reverse=True)
    q.sort(reverse=True)
    r.sort(reverse=True)
    heap_p = p[:X]
    heap_q = q[:Y]
    hq.heapify(heap_p)
    hq.heapify(heap_q)
    
    for ri in r:
        if heap_p[0] < ri and heap_p[0] <= heap_q[0]:
            hq.heappushpop(heap_p, ri)
        elif heap_q[0] < ri:
            hq.heappushpop(heap_q, ri)
        else:
            break
    
    ans = sum(heap_p) + sum(heap_q)
    print(ans)


if __name__ == '__main__':
    solve()
