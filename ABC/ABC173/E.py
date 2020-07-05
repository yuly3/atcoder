import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def mod_div(x, y, mod=10 ** 9 + 7):
    return x * pow(y, mod - 2, mod) % mod


def solve():
    N, K = map(int, rl().split())
    A = list(map(int, rl().split()))
    MOD = 10 ** 9 + 7
    
    if K == N:
        ans = 1
        for ai in A:
            ans *= ai
            ans %= MOD
        print(ans)
        return

    A.sort(key=lambda num: abs(num), reverse=True)
    if all(ai < 0 for ai in A) and K % 2 == 1:
        ans = 1
        for ai in A[-K:]:
            ans *= ai
            ans %= MOD
        print(ans)
        return
    
    ans = 1
    INF = 10 ** 10
    min_pos, min_neg = INF, INF
    cnt_neg = 0
    for ai in A[:K]:
        if ai < 0:
            min_neg = ai
            cnt_neg += 1
        else:
            min_pos = ai
        ans *= ai
        ans %= MOD
    
    if cnt_neg % 2 == 0:
        print(ans)
    else:
        n_pos, n_neg = INF, INF
        for ai in A[K:]:
            if n_pos != INF and n_neg != INF:
                break
            if ai < 0 and n_neg == INF:
                n_neg = ai
            elif 0 <= ai and n_pos == INF:
                n_pos = ai
        if min_pos != INF and min_neg != INF and n_pos != INF and n_neg != INF:
            if abs(min_pos * n_pos) <= abs(min_neg * n_neg):
                ans = mod_div(ans, min_pos) * n_neg % MOD
            else:
                ans = mod_div(ans, min_neg) * n_pos % MOD
        elif min_neg != INF and n_pos != INF:
            ans = mod_div(ans, min_neg) * n_pos % MOD
        else:
            ans = mod_div(ans, min_pos) * n_neg % MOD
        print(ans)


if __name__ == '__main__':
    solve()
