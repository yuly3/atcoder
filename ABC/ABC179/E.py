import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, X, M = map(int, rl().split())
    
    A = []
    idx = dict()
    cnt = 0
    while 1:
        if X in idx:
            roop_start = idx[X]
            roop_size = cnt - roop_start
            break
        A.append(X)
        idx[X] = cnt
        X = X ** 2 % M
        cnt += 1
    
    if N <= roop_start:
        print(sum(A[:N]))
        return
    
    roop_cnt, rem = divmod(N - roop_start, roop_size)
    ans = sum(A[:roop_start])
    ans += roop_cnt * sum(A[roop_start:roop_start + roop_size])
    ans += sum(A[roop_start:roop_start + rem])
    print(ans)


if __name__ == '__main__':
    solve()
