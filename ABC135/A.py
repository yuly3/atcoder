def solve():
    A, B = map(int, input().split())

    if (B - A) % 2 != 0:
        print('IMPOSSIBLE')
        exit()
    else:
        print((B + A) // 2)


if __name__ == '__main__':
    solve()