import sys


def solve():
    password = input()

    for i in range(3):
        if password[i] == password[i + 1]:
            print('Bad')
            sys.exit()

    print('Good')


if __name__ == '__main__':
    solve()