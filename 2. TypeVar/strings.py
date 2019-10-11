text="Hello, world"
print(len(text)) # количество симоволов 12
print(text[0]) # первый символ H
print(text[-1]) # последний символ d
print(text[3-5]) # что будет?

CARDNUMBER = 4242_1543_1456_0102
print(CARDNUMBER + 1) # 4242154314560103
print(str(CARDNUMBER) + "1") # 42421543145601021

i = "i love "
app1 = "w3af"
app2 = "nmap"
app3 = "metasploit"

print(i + app1, app2 , app3) # i love w3af nmap metasploit
print(i + app1+app2+app3) # i love w3afnmapmetasploit
print(i + app1,app2, app3, sep=", ") # i love w3af, nmap, metasploit
print(i + app1,app2, app3, sep=", ", end=".") # i love w3af, nmap, metasploit.
print(i + app1,app2, app3, sep=", ", end=".\n") # i love w3af, nmap, metasploit.
print(i, 'pentesting') # i love  pentesting






