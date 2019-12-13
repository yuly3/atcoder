def solve():
    N, *w = map(int, open(0).read().split())
    block = [w[0]]

    for i in range(1, N):
        min_dw = 100000
        j = -1
        for index, top in enumerate(block):
            dw = top - w[i]
            if 0 <= dw < min_dw:
                j = index
                min_dw = dw
        if j == -1:
            block.append(w[i])
        else:
            block[j] = w[i]

    print(len(block))


if __name__ == '__main__':
    solve()