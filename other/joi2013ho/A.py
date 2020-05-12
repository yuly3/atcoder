import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    A = list(map(int, rl().split()))
    
    d = []
    pa = A[0]
    cnt = 1
    for i in range(1, N):
        ca = A[i]
        if pa != ca:
            cnt += 1
            if i == N - 1:
                d.append(cnt)
        else:
            d.append(cnt)
            cnt = 1
        pa = ca
    
    len_d = len(d)
    if len_d == 1 or len_d == 2:
        print(N)
        return
    
    ans = 0
    for i in range(1, len_d - 1):
        ans = max(ans, d[i - 1] + d[i] + d[i + 1])
    print(ans)


if __name__ == '__main__':
    solve()
