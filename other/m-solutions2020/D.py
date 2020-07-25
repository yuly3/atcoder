import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    A = list(map(int, rl().split())) + [0]
    
    B = []
    left, right = 0, 1
    while right != N + 2:
        if A[left:right] == list(sorted(A[left:right])):
            right += 1
        else:
            B.append(A[left:right - 1])
            left = right - 1
    
    score = 1000
    for a_lr in B:
        if len(a_lr) == 1:
            continue
        stock, score = divmod(score, a_lr[0])
        score += stock * a_lr[-1]
    print(score)


if __name__ == '__main__':
    solve()
