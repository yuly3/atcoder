def solve():
    n = int(input())
    monsters = list(map(int, input().split()))
    heroes = list(map(int, input().split()))

    defeat = 0
    for i in range(n - 1, -1, -1):
        if monsters[i + 1] >= heroes[i]:
            defeat += heroes[i]
        else:
            defeat += monsters[i + 1]
            heroes[i] -= monsters[i + 1]
            if monsters[i] >= heroes[i]:
                defeat += heroes[i]
                monsters[i] -= heroes[i]
            else:
                defeat += monsters[i]
                monsters[i] = 0

    print(defeat)


if __name__ == '__main__':
    solve()
