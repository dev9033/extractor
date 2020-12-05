# extract names from details

import re

with open('data.txt') as f:
    content = f.read()
    # print(content)


def name():
    name = re.compile(r'([A-Z][a-z]+\s[A-Z][a-z]+(-[A-Z][a-z]+)?)'+'\n')
    matches = name.finditer(content)
    for match in matches:
        print('name-> ' + match.group(1))


def phone_number():
    phone = re.compile(r'\d{3}[.-]\d{3}[.-]\d{4}')
    matches = phone.findall(content)
    for match in matches:
        print(match)


def email():
    email = re.compile(r'([A-Za-z]+)(@[A-Za-z]+\.com)')
    matches = email.finditer(content)
    for match in matches:
        print('username-> '+match.group(1)+' + '+'domain-> '+match.group(2))


name()  # comment out if name is not needed
email()  # comment out if email is not needed
phone_number()  # comment out if phone number is not needed
