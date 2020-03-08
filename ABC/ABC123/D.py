import heapq


def solve():
    X, Y, Z, K = map(int, input().split())
    a_ls = sorted(map(lambda x: -int(x), input().split()))
    b_ls = sorted(map(lambda x: -int(x), input().split()))
    c_ls = sorted(map(lambda x: -int(x), input().split()))
    hq = []
    heapq.heappush(hq, (a_ls[0] + b_ls[0] + c_ls[0], 0, 0, 0))
    hq_hash = {(0, 0, 0)}
    
    for _ in range(K):
        ans, i, j, k = heapq.heappop(hq)
        
        if i + 1 < X and not ((i + 1, j, k) in hq_hash):
            hq_hash.add((i + 1, j, k))
            heapq.heappush(hq, (a_ls[i + 1] + b_ls[j] + c_ls[k], i + 1, j, k))
        if j + 1 < Y and not ((i, j + 1, k) in hq_hash):
            hq_hash.add((i, j + 1, k))
            heapq.heappush(hq, (a_ls[i] + b_ls[j + 1] + c_ls[k], i, j + 1, k))
        if k + 1 < Z and not ((i, j, k + 1) in hq_hash):
            hq_hash.add((i, j, k + 1))
            heapq.heappush(hq, (a_ls[i] + b_ls[j] + c_ls[k + 1], i, j, k + 1))
        
        print(-ans)


if __name__ == '__main__':
    solve()
