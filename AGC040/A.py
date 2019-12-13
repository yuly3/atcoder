def solve():
    s_arr = input().replace('><', '> <').split()
    ans = 0

    for s in s_arr:
        left = s.count('<')
        right = len(s) - left
        if left < right:
            left -= 1
            ans += left * (left + 1) // 2 + right * (right + 1) // 2
        else:
            right -= 1
            ans += left * (left + 1) // 2 + right * (right + 1) // 2

    print(ans)


if __name__ == '__main__':
    solve()