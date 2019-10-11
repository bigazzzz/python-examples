print("-"*10, "\n1 часть", "\n", "-"*10)
text="Hello, world"
print(len(text)) # количество симоволов 12
print(text[0]) # первый символ H
print(text[-1]) # последний символ d
print(text[3-5]) # что будет?

print("-"*10, "\n2 часть", "\n", "-"*10)
text="Hello, world"
print(text[1:5]) # ello
print(text[0:5]) # Hello
print(text[:5]) # Hello
print(text[-5:]) # world

print("-"*10, "\n3 часть", "\n", "-"*10)
CARDNUMBER = 4242_1543_1456_0102
print(CARDNUMBER + 1) # 4242154314560103
print(str(CARDNUMBER) + "1") # 42421543145601021

print("-"*10, "\n4 часть", "\n", "-"*10)
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
print((i+'pentesting'+' ')*5)
# i love pentesting i love pentesting i love pentesting i love pentesting i love pentesting






