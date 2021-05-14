import configparser

import requests as rq
from bs4 import BeautifulSoup, element

config = configparser.ConfigParser()
config.read('./config.ini')
USERID = config['USER']['userid']
PASSWORD = config['USER']['password']

base_url = 'https://manaba.fun.ac.jp/ct/'
url = base_url + 'login'
login_data = {
    'userid': USERID,
    'password': PASSWORD
}

session = rq.session()
session.get(url)

login = session.post(url, data=login_data)

bs = BeautifulSoup(login.text, 'lxml')
courses = bs.find_all('td', class_='course')
for course in courses:
    if course.find('a'):
        report_url = base_url + course.find('a').get('href') + '_report'
        report = BeautifulSoup(session.get(report_url).text, 'lxml')
        course_name = report.find('a', id='coursename').get_text()
        # if course.find('a').get('href') == 'course_96360':  # テストのため決め打ち
        print('-'*20)
        print(course_name)
        table = report.find_all('table', class_='stdlist')
        for row in table:
            row: element.Tag
            tasks: list[element.Tag] = row.find_all('tr')[1:]  # １つ目の課題
            for task in tasks:
                title: element.Tag
                state: element.Tag
                start: element.Tag
                end: element.Tag
                title, state, start, end = task.find_all('td')
                if state.find('div').get_text() == '受付中' and state.find('span', class_='deadline').get_text() == '未提出':
                    print(title.find('a').get_text())
                    print(state.find('span', class_='deadline').get_text())
                    print(start.get_text())
                    print(end.get_text())
                    