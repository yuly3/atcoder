def solve():
    N, M = map(int, input().split())
    s, c = [0] * M, [0] * M
    for i in range(M):
        s[i], c[i] = map(int, input().split())
    
    ans = 0
    while ans < 1000:
        str_ans = str(ans)
        len_str_ans = len(str(ans))
        if len_str_ans == N:
            cnt = 0
            for i in range(M):
                if len_str_ans < s[i]:
                    break
                if int(str_ans[(len_str_ans - 1) - (len_str_ans - s[i])]) == c[i]:
                    cnt += 1
            if cnt == M:
                print(ans)
                exit()
        ans += 1
    print(-1)


if __name__ == '__main__':
    solve()
