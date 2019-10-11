man_user = {"name": "Вася", "age": 17, "iq": 100}
woman_user = {"name": "Таня", "age": 37, "iq": 13}

text = "Я {user[name]}. Мне {user[age]} лет. Мой IQ = {user[iq]}"
print(text.format(user=man_user)) # Я Вася. Мне 17 лет. Мой IQ = 100
print(text.format(user=woman_user)) # Я Таня. Мне 37 лет. Мой IQ = 13
