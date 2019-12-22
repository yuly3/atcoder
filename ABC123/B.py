def solve():
    dishes = list(map(int, open(0).read().split()))
    
    last = 0
    dt_max = 0
    for i in range(5):
        if dishes[i] % 10 != 0 and dt_max <= 10 - (dishes[i] - dishes[i] // 10 * 10):
            dt_max = 10 - (dishes[i] - dishes[i] // 10 * 10)
            last = i
    
    ans = 0
    for i in range(5):
        if i != last:
            if dishes[i] % 10 != 0:
                ans += 10 * (dishes[i] // 10 + 1)
            else:
                ans += dishes[i]
        else:
            ans += dishes[i]
    print(ans)


if __name__ == '__main__':
    solve()
