def solve():
    N = int(input())
    a = list(map(int, input().split()))
    
    max_idx, min_idx = -1, -1
    max_a, min_a = -10 ** 6, 10 ** 6
    for i, ai in enumerate(a):
        if max_a < ai:
            max_a = ai
            max_idx = i
        if ai < min_a:
            min_a = ai
            min_idx = i
    
    ans = []
    if abs(min_a) <= abs(max_a):
        for i in range(N):
            ans.append([max_idx + 1, i + 1])
        for i in range(N - 1):
            ans.append([i + 1, i + 2])
    else:
        for i in range(N):
            ans.append([min_idx + 1, i + 1])
        for i in range(N, 1, -1):
            ans.append([i, i - 1])
    
    print(len(ans))
    for x, y in ans:
        print(x, y)


if __name__ == '__main__':
    solve()
