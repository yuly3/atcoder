import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    S = rl().rstrip()
    
    j_acc, o_acc, i_acc = [0] * (N + 1), [0] * (N + 1), [0] * (N + 1)
    for i in range(N):
        si = S[i]
        j_acc[i + 1] = j_acc[i] + (si == 'J')
        o_acc[i + 1] = o_acc[i] + (si == 'O')
        i_acc[i + 1] = i_acc[i] + (si == 'I')
    
    init_cmb = 0
    for i in range(N):
        if S[i] == 'O':
            init_cmb += j_acc[i] * (i_acc[-1] - i_acc[i + 1])
    
    ans = init_cmb + sum(o_acc[i] for i in range(1, N + 1) if i_acc[i] != i_acc[i - 1])
    for i in range(1, N):
        ans = max(ans, init_cmb + j_acc[i] * (i_acc[-1] - i_acc[i]))
    ans = max(ans, init_cmb + sum(j_acc[i] for i in range(1, N + 1) if o_acc[i] != o_acc[i - 1]))
    print(ans)


if __name__ == '__main__':
    solve()
