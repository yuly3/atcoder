def solve():
    N, *T = map(int, open(0).read().split())

    bottleneck = (0, 10**15)
    for i, t in enumerate(T):
        if t <= bottleneck[1]:
            bottleneck = (i, t)
    
    if N % bottleneck[1] == 0:
        print(bottleneck[0] + N // bottleneck[1] + 4 - bottleneck[0])
    else:
        print(bottleneck[0] + N // bottleneck[1] + 1 + 4 - bottleneck[0])


if __name__ == '__main__':
    solve()
