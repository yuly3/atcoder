import sys


def solve():
    step = input()

    for i in range(len(step)):
        if i % 2 == 0:
            if step[i] != 'R' and step[i] != 'U' and step[i] != 'D':
                print('No')
                sys.exit()
        else:
            if step[i] != 'L' and step[i] != 'U' and step[i] != 'D':
                print('No')
                sys.exit()

    print('Yes')


if __name__ == '__main__':
    solve()
