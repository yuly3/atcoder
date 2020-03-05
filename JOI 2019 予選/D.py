from operator import itemgetter


def solve():
    N, *A = map(int, open(0).read().split())
    
    B = sorted(zip(A, range(1, N + 1)), key=itemgetter(0))
    island = [False] * (N + 2)
    island[0] = island[-1] = True
    
    cnt = 0
    A = [0] + A + [0]
    for i in range(N + 1):
        if A[i] == 0:
            island[i] = True
            if 0 < A[i + 1]:
                cnt += 1
    ans, tmp = cnt, cnt
    
    B.append((-1, 0))
    for i in range(N):
        b, idx = B[i]
        if b == 0:
            continue
        
        if island[idx - 1] and island[idx + 1]:
            tmp -= 1
        elif not island[idx - 1] and not island[idx + 1]:
            tmp += 1
        if b != B[i + 1][0]:
            ans = max(ans, tmp)
        island[idx] = True
    print(ans)


if __name__ == '__main__':
    solve()
