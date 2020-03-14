def solve():
    N = int(input())
    X = list(map(int, input().split()))
    
    sorted_X = sorted(X)
    mid_l = sorted_X[N // 2 - 1]
    mid_r = sorted_X[N // 2]
    
    for xi in X:
        if xi <= mid_l:
            print(mid_r)
        else:
            print(mid_l)


if __name__ == '__main__':
    solve()
