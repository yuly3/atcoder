def solve():
    r, D, x = map(int, input().split())
    
    ans = x
    for i in range(10):
        ans = r * ans - D
        print(ans)


if __name__ == '__main__':
    solve()