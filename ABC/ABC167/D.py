import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, K = map(int, rl().split())
    A = list(map(int, rl().split()))
    
    pos = dict()
    for idx, ai in enumerate(A):
        pos[ai] = idx + 1
    
    u_set = set()
    u_set.add(1)
    counter = dict()
    counter[1] = 0
    ca = A[0]
    cnt = 1
    roop_s = 0
    b = 0
    while 1:
        if ca in u_set:
            if ca == roop_s:
                roop = cnt - counter[ca]
                break
            elif roop_s == 0:
                counter[ca] = cnt
                roop_s = ca
                b = cnt
        u_set.add(ca)
        ca = A[ca - 1]
        cnt += 1
    
    if K < b:
        ca = A[0]
        cnt = 1
        while 1:
            if cnt == K:
                ans = ca
                break
            ca = A[ca - 1]
            cnt += 1
    else:
        m = (K - b) % roop
        ca = A[pos[roop_s] - 1]
        cnt = 0
        while 1:
            if cnt == m:
                ans = ca
                break
            ca = A[ca - 1]
            cnt += 1
    print(ans)


if __name__ == '__main__':
    solve()
