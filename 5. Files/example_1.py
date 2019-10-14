wordlist_file = open("wordlist_utf8.txt", encoding="utf-8")
wordlist = wordlist_file.read()
print(wordlist)

wordlist_file = open("wordlist_cp1251.txt")
wordlist = wordlist_file.read()
print(wordlist)
