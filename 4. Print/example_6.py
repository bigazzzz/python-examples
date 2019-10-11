man_user = ["Вася", 17, 100]
woman_user = ["Таня", 37, 33]
text = "Я {user[0]}. Мне {user[1]} лет. Мой IQ = {user[2]}"
print(text.format(user=man_user)) # Я Вася. Мне 17 лет. Мой IQ = 100
print(text.format(user=woman_user)) # Я Таня. Мне 37 лет. Мой IQ = 33
