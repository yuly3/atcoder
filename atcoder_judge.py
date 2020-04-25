import os
import sys
import requests
import subprocess
from bs4 import BeautifulSoup

LOGIN_URL = 'https://atcoder.jp/login?continue=https%3A%2F%2Fatcoder.jp%2Fcontests%2F'
CONTEST_URL = 'https://atcoder.jp/contests/'
TESTCASES_PATH = 'testcase'
TLE_TIME = 2


def analyze_page(page_org):
    page = BeautifulSoup(page_org.text, 'lxml').find_all(class_='part')
    question_list = []
    question = {}
    for element in page:
        ele_h3 = element.findChild('h3')
        ele_pre = element.findChild('pre')
        if 'Sample' not in str(ele_h3):
            continue
        if 'Input' in str(ele_h3):
            question = {'input': str(ele_pre).lstrip('<pre>').rstrip('</pre>').replace('\r\n', '\n')}
        else:
            question['output'] = str(ele_pre).lstrip('<pre>').rstrip('</pre>').replace('\r\n', '\n')
            question_list.append(question)
            question = {}
    return question_list


def path_check(directory_name):
    return os.path.exists('./' + directory_name)


def file_write(test_cases_path, file_name, test_cases):
    target_path = os.path.join(test_cases_path, file_name)
    with open(target_path, 'w') as f:
        for i, query in enumerate(test_cases):
            f.write('test case' + str(i + 1) + '\n')
            f.write('input\n')
            f.write(query['input'])
            f.write('output\n')
            f.write(query['output'])
            f.write('--end--\n')


def read_file(test_cases_path, file_name):
    test_cases = []
    test_case = {}
    mode = ''
    target_path = os.path.join(test_cases_path, file_name)
    with open(target_path, 'r') as f:
        while 1:
            line = f.readline().rstrip('\r\n')
            if 'test case' in line:
                test_case = {}
                continue
            if 'input' in line:
                mode = 'input'
                test_case[mode] = ''
                continue
            if 'output' in line:
                mode = 'output'
                test_case[mode] = ''
                continue
            if '--end--' in line:
                test_cases.append(test_case)
                continue
            if not line:
                break
            test_case[mode] += line + '\n'
    return test_cases


class ManageTestCases:
    def __init__(self, contest_name, contest_num, user_name, password):
        self.contest = contest_name + contest_num
        self.user_name = user_name
        self.password = password
    
    def get_test_cases(self, question_name):
        test_cases_path = TESTCASES_PATH + '/' + self.contest
        if not path_check(test_cases_path):
            os.mkdir(test_cases_path)
        file_name = question_name + '.in'
        if file_name in os.listdir(test_cases_path):
            test_cases = read_file(test_cases_path, file_name)
        else:
            test_cases = self.__scrape_page(question_name)
            file_write(test_cases_path, file_name, test_cases)
        return test_cases

    def __scrape_page(self, question_name):
        session = requests.session()
        self.__login_page(session)
        page = session.get(CONTEST_URL + self.contest + '/tasks/' + self.contest + '_' + question_name)
        test_cases = analyze_page(page)
        return test_cases
    
    def __login_page(self, session):
        res = session.get(LOGIN_URL + self.contest)
        page = BeautifulSoup(res.text, 'lxml')
        csrf_token = page.find(attrs={'name': 'csrf_token'}).get('value')
        login_info = {
            'csrf_token': csrf_token,
            'username': self.user_name,
            'password': self.password,
        }
        session.post(LOGIN_URL + self.contest, data=login_info)


class ExecuteTestCases:
    def __init__(self, contest_name, contest_num, question_name, test_cases):
        self.contest_name = contest_name
        self.contest = contest_name + contest_num
        self.question_name = question_name
        self.test_cases = test_cases
    
    def execute(self):
        print('Judging ' + self.contest + ' ' + self.question_name)
        self.__run()
    
    def __run(self):
        contest_dir = self.contest_name.upper() + '/' + self.contest.upper()
        cmd = 'python ./' + contest_dir + '/' + self.question_name.upper() + '.py'
        for i, test_case in enumerate(self.test_cases):
            print('test case' + str(i + 1) + ': ', end='')
            proc = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE, stdin=subprocess.PIPE)
            proc.stdin.write(test_case['input'].encode())
            proc.stdin.flush()
            proc.stdout.flush()
            # noinspection PyBroadException
            try:
                proc.wait(TLE_TIME)
                ans = proc.stdout.read().decode().replace('\r\n', '\n')
                out = test_case['output']
                if out == ans:
                    print('AC')
                else:
                    print('WA')
                    print('your answer:   ' + ans + 'correct answer:' + out)
            except:
                print('TLE')
                proc.terminate()


if __name__ == '__main__':
    g_contest_name, g_contest_num, g_question_name = sys.argv[1:]
    g_user_name, g_password = os.environ['ATCODER_USER_NAME'], os.environ['ATCODER_PASSWORD']
    test_cases_manager = ManageTestCases(g_contest_name, g_contest_num, g_user_name, g_password)
    test_cases_data = test_cases_manager.get_test_cases(g_question_name)
    
    test_cases_executer = ExecuteTestCases(g_contest_name, g_contest_num, g_question_name, test_cases_data)
    test_cases_executer.execute()
