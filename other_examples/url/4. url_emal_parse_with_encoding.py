import requests
import re
url = input('url=>')
r = requests.get(url)
htmlfile = open('site.html','w+',encoding=r.encoding)
htmlfile.write(r.text)
htmlfile.close()
email_pattern = r'href="mailto:(\S+)"'
mailfile = open('emails.txt','w+',encoding=r.encoding)
for email in re.findall(email_pattern, r.text):
	mailfile.write(email + '\n')
mailfile.close()
url_pattern = r'href="(\S+)"'
urlfile = open('urls.txt','w+',encoding=r.encoding)
for url in re.findall(url_pattern, r.text):
	urlfile.write(url + '\n')
urlfile.close()
