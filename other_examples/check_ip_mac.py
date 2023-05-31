import re

text = input()
pattern_ip = r'(\d{1,3}\.){3}\d{1,3}'
pattern_mac = r'([a-fA-F0-9]{2}[:-]){5}' \
              r'[a-fA-F0-9]{2}'

if re.fullmatch(pattern_ip,text) != None:
    print(re.fullmatch(pattern_ip,text).group() + ' is Ip-адрес')
elif re.fullmatch(pattern_mac, text) != None:
    print(re.fullmatch(pattern_mac,text).group() + ' is mac-адрес')
else:
    print('this is text')
