from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from json import load

email = input('Email: ').strip()
username = input("Username: ").strip()
password = input('Password: (enter to use configured password) ').strip()
dateofbirth = input(
    'Date of birth: (dd/mm/yy eg: 1/1/1970) (enter to use configured date of birth) ').strip()


class validate:

    def __init__(self) -> None:
        pass

    def email(email):
        if not email:
            raise ValueError('Please enter an email')
        elif not '@' in email:
            raise ValueError('Please enter a valid email')
        else:
            return email

    def username(username):
        if not username:
            raise ValueError('Please enter an username')
        else:
            return username

    def password(password):
        if not password:
            default_password = load(open('config.json'))['password']
            return default_password
        elif len(password) < 8:
            raise ValueError(
                "Please use password with characters length of more than 8")
        else:
            return password

    def date_of_birth(date_of_birth):
        if not date_of_birth:
            return load(open('config.json'))['date_of_birth']
        elif len(date_of_birth) > 10 or len(date_of_birth) < 8:
            raise SyntaxError('Please use the correct syntax')
        elif int(date_of_birth[-4:]) not in list(range(1950, 2009)):
            raise ValueError('Please use correct birth of date')
        elif int(date_of_birth[-4:]) in list(range(2009, 2024)):
            raise ValueError('You must be 13 years old to use discord')
        elif not '/' in date_of_birth:
            raise SyntaxError('Please follow the correct syntax')
        else:
            return str(date_of_birth)

    def day():
        day = validate.date_of_birth(dateofbirth).split('/')[0]
        if int(day) in list(range(1, 32)):
            return int(day)
        else:
            raise ValueError("Date of month cannot exceed 31")

    def month():
        month = validate.date_of_birth(dateofbirth).split('/')[1]
        if int(month) in list(range(1, 13)):
            return int(month)
        else:
            raise ValueError("Month of year cannot exceed 12")

    def year():
        year = validate.date_of_birth(dateofbirth)[-4:]
        if int(year[-1]) in list(range(1, 9)):
            return (21 - int(year[-1]))
        elif int(year[-4]) == 1:
            if int(year[-2:]) in list(range(50, 100)):
                return 22 + (99 - int(year[-2:]))
        else:
            return 21


username = (validate.username(username))
password = (validate.password(password))
email = (validate.email(email))
day = validate.day()
month = validate.month()
year = validate.year()
chrome = webdriver.Chrome()
chrome.get("https://discord.com/register")
time.sleep(5)
actions = ActionChains(chrome)
actions.send_keys(email, Keys.TAB, username, Keys.TAB, password,
                  Keys.TAB, Keys.DOWN*month, Keys.TAB, Keys.DOWN*day, Keys.TAB, Keys.DOWN*year, Keys.TAB*3)

actions.perform()
print("Session will be closed in one hour")
time.sleep(3600)
print("Session closed")