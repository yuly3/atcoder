def solve():
    N, M = map(int, input().split())
    ab = [[0, 0] for _ in range(M)]
    for i in range(M):
        ab[i] = list(map(int, input().split()))
    ab.sort(key=lambda x: x[1])

    ans = 0
    p_except = 0
    for a, b in ab:
        if a <= p_except:
            continue
        p_except = b - 1
        ans += 1

    print(ans)


if __name__ == '__main__':
    solve()