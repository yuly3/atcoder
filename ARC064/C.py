def solve():
    N, x, *a = map(int, open(0).read().split())
    
    p_sum_a = sum(a)
    
    if x < a[0]:
        a[0] = x
    
    for i in range(1, N):
        if x < a[i-1] + a[i]:
            a[i] = x - a[i-1]
    
    sum_a = sum(a)
    print(p_sum_a - sum_a)


if __name__ == '__main__':
    solve()
