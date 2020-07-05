import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    A = list(map(int, rl().split()))
    
    A.sort(reverse=True)
    B = [A[0]]
    for ai in A[1:]:
        B += [ai, ai]
    ans = sum(B[:N - 1])
    print(ans)


if __name__ == '__main__':
    solve()
