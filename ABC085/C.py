def solve():
    N, Y = map(int, input().split())

    for x in range(N+1):
        for y in range(N+1-x):
            if (Y - x*10000 - y*5000) % 1000 == 0:
                z = (Y - x*10000 - y*5000) // 1000
                if x + y + z == N:
                    print(x, y, z)
                    exit()

    print(-1, -1, -1)


if __name__ == '__main__':
    solve()