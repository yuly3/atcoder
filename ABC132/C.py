def solve():
    N, *d_l = map(int, open(0).read().split())
    d_l.sort()

    if d_l[N//2] == d_l[N//2-1]:
        print(0)
    else:
        print(d_l[N//2] - d_l[N//2-1])



if __name__ == '__main__':
    solve()