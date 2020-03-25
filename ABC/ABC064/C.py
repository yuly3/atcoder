def solve():
    _ = int(input())
    a = list(map(int, input().split()))
    
    counter = [0] * 9
    for ai in a:
        counter[min(8, ai // 400)] += 1
    
    ans_min = 0
    for i in range(8):
        if 0 < counter[i]:
            ans_min += 1
    
    ans_max = ans_min + counter[-1]
    if ans_min == 0:
        ans_min = 1
    print(ans_min, ans_max)


if __name__ == '__main__':
    solve()
