import requests as rq
from bs4 import BeautifulSoup

USERID = ''
PASSWORD = ''

base_url = 'https://manaba.fun.ac.jp/ct/'
url = base_url + 'login'
login_data = {
    'userid': USERID,
    'password': PASSWORD
}

session = rq.session()
session.get(url)

login = session.post(url, data=login_data)
# print(login.text)

bs = BeautifulSoup(login.text, 'lxml')
# print(bs)
courses = bs.find_all('td', class_='course')
print(len(courses))
for course in courses:
    if course.a:
        print(course.a.get('href'), course.a.text)
    # break
        c = session.get(base_url + course.a.get('href'))
        print(c)
