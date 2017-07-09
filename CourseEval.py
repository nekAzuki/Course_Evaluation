# this script allows login to UW web services
import requests
from bs4 import BeautifulSoup

# login info here
account = input("UW NetID: ")
password = input("Password: ")
login_info = {'user': account,
              'pass': password,
              'submit': 'Sign in'
              }
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}

# get web page
r = requests.get('https://weblogin.washington.edu/', headers=headers)

# parse web page
soup = BeautifulSoup(r.text, 'html5lib')
tags = soup.find_all(name='input', type='hidden')
# fill the login info form
for tag in tags:
    attrs = tag.attrs
    login_info[attrs['name']] = attrs['value']

#print(login_info)
# login
r = requests.post('https://weblogin.washington.edu/', data=login_info, headers=headers)

# save cookie for later use
cookie = r.cookies
r = requests.get('https://www.washington.edu/cec/summary.html', headers=headers, cookies=cookie)

soup = BeautifulSoup(r.text, 'html5lib')
jsButton = {'go' : 'Continue'}
tags = soup.find_all(name='input', type='hidden')

for tag in tags:
    attrs = tag.attrs
    jsButton[attrs['name']] = attrs['value']
print(jsButton)


# r = requests.post('https://www.washington.edu/cec/', headers=headers,data=jsButton)
#
# print(r.text)
