import requests

url = input('url=>')
format = input('format=>')
r = requests.get(url)
text = r.text
index = 0
while text.find(format+":", index) >= 0:
    start_pos = text.find(format+":", index)+len(format)+1
    end_pos = text.find("\"",start_pos)
    print(text[start_pos:end_pos])
    index = end_pos
