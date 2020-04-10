import os
import sys
from shutil import copyfile


def path_check(directory_name):
    return os.path.exists('./' + directory_name)


def main(contest_name, contest_number):
    if contest_name == 'abc':
        new_contest = 'ABC/ABC' + contest_number
        if path_check(new_contest):
            print('This contest is already there.')
            return
        os.mkdir(new_contest)
        for i in range(6):
            new_problem = chr(ord('A') + i) + '.py'
            copyfile('./template.py', './' + new_contest + '/' + new_problem)
        print('Done.')


if __name__ == '__main__':
    name, number = sys.argv[1:]
    main(name, number)
