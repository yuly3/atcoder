def solve():
    N, *W = map(int, open(0).read().split())
    left, right = W[0], sum(W[1:])
    ans = abs(left - right)
    for i in range(1, N-1):
        left += W[i]
        right -= W[i]
        ans = min(ans, abs(left - right))
    print(ans)


if __name__ == '__main__':
    solve()