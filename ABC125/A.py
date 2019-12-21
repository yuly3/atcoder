def solve():
    A, B, T = map(int, input().split())
    
    i = 0
    while (i+1)*A <= T:
        i += 1
    print(i*B)


if __name__ == '__main__':
    solve()
