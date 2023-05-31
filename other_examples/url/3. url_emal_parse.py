import requests
import re
'''Записываем в файл
'''
url = input('url=>')
r = requests.get(url)
htmlfile = open('site.html','w+')
htmlfile.write(r.text)
htmlfile.close()
'''Режем emails и пишем в текстовый файл
'''
email_pattern = r'href="mailto:(\S+)"'
mailfile = open('emails.txt','w+')
for email in re.findall(email_pattern, r.text):
	mailfile.write(email + '\n')
mailfile.close()
'''Режем href и пишем в текстовый файл
'''
url_pattern = r'href="(\S+)"'
urlfile = open('urls.txt','w+')
for url in re.findall(url_pattern, r.text):
	urlfile.write(url + '\n')
urlfile.close()
