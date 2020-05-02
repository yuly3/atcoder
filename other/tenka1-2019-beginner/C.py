import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    S = input()
    
    w_acc, b_acc = [0], [0]
    for i in range(N):
        w_acc.append(w_acc[-1] + (S[i] == '.'))
        b_acc.append(b_acc[-1] + (S[i] == '#'))
    
    ans = w_acc[-1]
    for i in range(1, N + 1):
        ans = min(ans, b_acc[i] + w_acc[-1] - w_acc[i])
    print(ans)


if __name__ == '__main__':
    solve()
