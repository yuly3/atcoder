import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = rl().rstrip()
    
    ans = 20
    stack = [(0, 0, 0)]
    while stack:
        s_num, n_idx, cnt = stack.pop()
        if n_idx == len(N):
            if s_num != 0 and s_num % 3 == 0:
                ans = min(ans, cnt)
            continue
        stack.append((s_num + int(N[n_idx]), n_idx + 1, cnt))
        stack.append((s_num, n_idx + 1, cnt + 1))
    print(ans if ans != 20 else -1)


if __name__ == '__main__':
    solve()
