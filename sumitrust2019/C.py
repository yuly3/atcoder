def solve():
    X = int(input())
    
    n = X // 100
    if X - n * 100 <= n * 5:
        print(1)
    else:
        print(0)


if __name__ == '__main__':
    solve()
