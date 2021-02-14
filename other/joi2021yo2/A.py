import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, A = map(int, rl().split())
    S = rl().rstrip()
    
    left_items = []
    for i, si in enumerate(S[:A - 1]):
        if si == '#':
            left_items.append(i)
    right_items = []
    for i, si in enumerate(S[A:]):
        if si == '#':
            right_items.append(A + i)
    right_items.reverse()
    
    ans = 0
    i = 0
    cur = A - 1
    while left_items or right_items:
        if i % 2 == 0:
            if not right_items:
                ans += N - cur
                cur = N
            else:
                m = right_items.pop()
                ans += m - cur
                cur = m
        else:
            if not left_items:
                ans += cur + 1
                cur = -1
            else:
                m = left_items.pop()
                ans += cur - m
                cur = m
        i += 1
    print(ans)


if __name__ == '__main__':
    solve()
