def solve():
    N = int(input())
    
    ans = int(N * 100 / 108)
    if int(ans * 1.08) == N:
        print(ans)
    elif int((ans + 1) * 1.08) == N:
        print(ans + 1)
    else:
        print(':(')


if __name__ == '__main__':
    solve()
