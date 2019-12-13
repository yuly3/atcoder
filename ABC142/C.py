def solve():
    N, *al = map(int, open(0).read().split())
    a_dic = {}

    for i in range(N):
        a_dic[i + 1] = al[i]

    a_dic_soted = sorted(a_dic.items(), key=lambda x: x[1])

    for i in a_dic_soted:
        print(i[0], end=' ')


if __name__ == '__main__':
    solve()
