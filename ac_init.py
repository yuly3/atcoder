import argparse
import os
from shutil import copyfile


def path_check(directory_name):
    return os.path.exists('./' + directory_name)


def make_contest_dir(contest_name, contest_num, extention):
    if contest_num != '':
        new_contest = contest_name.upper() + '/' + contest_name.upper() + contest_num
    else:
        new_contest = 'other/' + contest_name
    if path_check(new_contest):
        print('This contest is already there.')
        return
    print('Making ' + new_contest)
    os.mkdir(new_contest)
    for i in range(8):
        new_problem = chr(ord('A') + i) + '.' + extention
        copyfile('./template.' + extention, './' + new_contest + '/' + new_problem)
    print('Done')


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('contest_name')
    parser.add_argument('-n', '--contest_num', default='')
    parser.add_argument('-e', '--extention', default='nim')
    
    return parser.parse_args()


if __name__ == '__main__':
    exe_args = get_args()
    
    g_contest_num = exe_args.contest_num
    if g_contest_num != '':
        g_contest_num = g_contest_num.zfill(3)
    
    make_contest_dir(exe_args.contest_name, g_contest_num, exe_args.extention)
