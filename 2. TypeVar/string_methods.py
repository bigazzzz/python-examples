text = "HELLo, wORld!"
print(text.replace("w","W")) # HELLo, WORld!
print(text.lower()) # hello, world!
print(text.capitalize()) # Hello, world!
print(text.title()) # Hello, World!
print(text.lower().replace('world', 'pentester').upper())
# HELLO, PENTESTER!

domain1 = "bigazzzz.ru"
domain2 = "www.rutube.ru"
domain3 = "example.org"

print(domain1.find(".ru")) # 8
print(domain2.find(".ru")) # 3
print(domain3.find(".ru")) # -1

print(domain1.endswith(".ru")) # true
print(domain2.endswith(".ru")) # true
print(domain3.endswith(".ru")) # false

