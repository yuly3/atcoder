S = input()
num = []
ans = 0
length = 0


def calc(x, i, j):
    if i == length-1:
        x += j
        global ans
        ans += x
    else:
        calc(x+j, i+1, num[i+1])
        calc(x, i+1, 10*j+num[i+1])


def solve():
    for s in S:
        num.append(int(s))
    global length
    length = len(num)
    calc(0, 0, num[0])
    print(ans)


if __name__ == '__main__':
    solve()