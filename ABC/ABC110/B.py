def solve():
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    
    max_x = max(X, max(x))
    min_y = min(Y, min(y))
    if max_x < min_y:
        print('No War')
    else:
        print('War')


if __name__ == '__main__':
    solve()
