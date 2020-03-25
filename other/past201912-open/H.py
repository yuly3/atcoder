import sys

rl = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)


def solve():
    N = int(rl())
    C = [0] + list(map(int, rl().split()))
    
    min_odd, min_even = 10 ** 9, 10 ** 9
    cnt_odd = 0
    for i in range(1, N + 1):
        if i % 2 == 0:
            min_even = min(min_even, C[i])
        else:
            min_odd = min(min_odd, C[i])
            cnt_odd += 1
    
    ans = 0
    odd, even = 0, 0
    Q = int(rl())
    for i in range(Q):
        cmd, *xa = rl().split()
        if cmd == '1':
            x, a = map(int, xa)
            if x % 2 == 0:
                if a <= C[x] - even:
                    C[x] -= a
                    ans += a
                    min_even = min(min_even, C[x] - even)
            else:
                if a <= C[x] - odd:
                    C[x] -= a
                    ans += a
                    min_odd = min(min_odd, C[x] - odd)
        elif cmd == '2':
            a = int(xa[0])
            if a <= min_odd:
                ans += cnt_odd * a
                odd += a
                min_odd -= a
        else:
            a = int(xa[0])
            if a <= min_odd and a <= min_even:
                ans += N * a
                odd += a
                even += a
                min_odd -= a
                min_even -= a
    print(ans)


if __name__ == '__main__':
    solve()
