string = input("Введите строку - ")
char_number = input("Введите число - ")
char_number = int(char_number)

print(string[:char_number-1] + string[char_number-1].upper() + string[char_number:])
