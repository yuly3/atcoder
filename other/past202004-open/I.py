import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    A = [(int(ai), idx) for idx, ai in enumerate(rl().split())]
    
    ans = [0] * 2 ** N
    cnt = 1
    while cnt <= N:
        tmp_ls = []
        for i in range(0, len(A), 2):
            x_pow, x_num = A[i]
            y_pow, y_num = A[i + 1]
            if x_pow < y_pow:
                tmp_ls.append((y_pow, y_num))
                ans[x_num] = cnt
            else:
                tmp_ls.append((x_pow, x_num))
                ans[y_num] = cnt
        cnt += 1
        A = tmp_ls
    
    _, champ = A[0]
    ans[champ] = N
    print(*ans, sep='\n')


if __name__ == '__main__':
    solve()
