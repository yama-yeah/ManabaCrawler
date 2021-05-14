import configparser
from dataclasses import dataclass

import requests as rq
from bs4 import BeautifulSoup, element


@dataclass
class Task:
    id: int
    title: str
    state: str
    start: str
    end: str


Tasks = list[Task]


@dataclass
class Course:
    "コース"
    course_name: str
    tasks: Tasks


Courses = list[Course]


def main():
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

    couses_have_tasks = Courses()

    bs = BeautifulSoup(login.text, 'lxml')
    courses = bs.find_all('td', class_='course')
    for course in courses:
        if course.find('a'):
            report_url: str = base_url + course.find('a').get('href') + '_report'
            report = BeautifulSoup(session.get(report_url).text, 'lxml')
            course_name: str = report.find('a', id='coursename').get_text()
            table = report.find_all('table', class_='stdlist')
            for row in table:
                row: element.Tag
                reports: list[element.Tag] = row.find_all('tr')[1:]
                un_submitted_tasks = Tasks()
                for item in reports:
                    title: element.Tag
                    state: element.Tag
                    start: element.Tag
                    end: element.Tag
                    title, state, start, end = item.find_all('td')
                    if state.find('div').get_text() == '受付中' and state.find('span', class_='deadline').get_text() == '未提出':
                        t = Task(
                            id=int(title.find('a').get('href').split('_')[-1]),
                            title=title.find('a').get_text(),
                            state=state.find(
                                'span', class_='deadline').get_text(),
                            start=start.get_text(),
                            end=end.get_text()
                        )
                        un_submitted_tasks.append(t)
                couses_have_tasks.append(Course(course_name=course_name, tasks=un_submitted_tasks))

    for item in couses_have_tasks:
        print(item)

if __name__ == '__main__':
    main()