def solve():
    N, *sl = map(lambda x: ''.join(sorted(x)), open(0).read().split())
    dic = {}
    ans = 0

    for s in sl:
        if s in dic:
            ans += dic[s]
            dic[s] += 1
        else:
            dic[s] = 1

    print(ans)


if __name__ == '__main__':
    solve()
