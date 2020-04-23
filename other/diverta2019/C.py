import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    s = [input() for _ in range(N)]
    
    ans = 0
    cnt_a, cnt_b, cnt_ab = 0, 0, 0
    for si in s:
        ans += si.count('AB')
        if si[-1] == 'A' and si[0] == 'B':
            cnt_ab += 1
        elif si[-1] == 'A':
            cnt_a += 1
        elif si[0] == 'B':
            cnt_b += 1
    
    if cnt_ab == 0:
        ans += min(cnt_a, cnt_b)
    else:
        if 0 < cnt_a + cnt_b:
            ans += cnt_ab + min(cnt_a, cnt_b)
        else:
            ans += cnt_ab - 1
    print(ans)


if __name__ == '__main__':
    solve()
