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
