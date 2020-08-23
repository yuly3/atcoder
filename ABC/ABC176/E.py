import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    H, W, M = map(int, rl().split())
    hw = [list(map(lambda n: int(n) - 1, rl().split())) for _ in range(M)]
    
    sum_h, sum_w = [0] * H, [0] * W
    for h, w in hw:
        sum_h[h] += 1
        sum_w[w] += 1
    max_h, max_w = max(sum_h), max(sum_w)
    cnt = sum_h.count(max_h) * sum_w.count(max_w)
    
    for h, w in hw:
        if sum_h[h] == max_h and sum_w[w] == max_w:
            cnt -= 1
    ans = max_h + max_w
    print(ans if cnt else ans - 1)


if __name__ == '__main__':
    solve()
