import httplib2

url = input('url=>')
h = httplib2.Http(".cache")
resp, content = h.request(url, "GET")
htmlfile = open('site.html','w+',encoding='utf-8')
htmlfile.write(content.decode('utf-8'))
htmlfile.close()
