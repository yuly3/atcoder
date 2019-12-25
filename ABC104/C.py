D, G = map(int, input().split())
p = [0 for _ in range(D)]
c = [0 for _ in range(D)]
for i in range(D):
    p[i], c[i] = map(int, input().split())

score_sum = [0 for _ in range(D)]
for i in range(D):
    score_sum[i] = (i + 1) * 100 * p[i] + c[i]


def calc(i, g):
    if g <= 0:
        return 0
    if i == D:
        return 10 ** 7
    
    x = calc(i + 1, g)
    y = p[i] + calc(i + 1, g - score_sum[i])
    upper_sum = sum(score_sum[i + 1:])
    if 100 * (i + 1) * p[i] + upper_sum < g:
        z = 10 ** 7
    else:
        z = sum(p[i + 1:]) + max(0, (g - upper_sum + 100 * (i + 1) - 1) // (100 * (i + 1)))
    return min(x, y, z)


def solve():
    ans = calc(0, G)
    print(ans)


if __name__ == '__main__':
    solve()
