from collections import defaultdict


def solve():
    N, M, *A = map(int, open(0).read().split())
    
    cumsum = [0] * (N + 1)
    for i in range(N):
        cumsum[i + 1] = cumsum[i] + A[i]
    
    mods = defaultdict(int)
    for num in cumsum:
        mods[num % M] += 1
    
    ans = 0
    for val in mods.values():
        ans += val * (val - 1) // 2
    print(ans)


if __name__ == '__main__':
    solve()
