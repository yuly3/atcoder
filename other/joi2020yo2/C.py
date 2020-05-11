import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    
    tgt = {N}
    ans = 1
    for num in range(N - 1, 0, -1):
        dsm = sum(int(di) for di in str(num))
        if num + dsm in tgt:
            tgt.add(num)
            ans += 1
    print(ans)


if __name__ == '__main__':
    solve()
