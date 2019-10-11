name = "Вася"
age = 17
iq = 53.5
pi = 3.141592

index_text = "Я {0}. Мне {1} лет. Мой IQ = {2}. Я знаю, что ПИ={3}".format(name, age, iq, pi)
name_text = "Я {user_name}. Мне {user_age} лет. Мой IQ = {user_iq}. Я знаю, что ПИ={pi}" \
    .format(user_name=name, user_age=age, user_iq=iq, pi=pi)
print(index_text) # Я Вася. Мне 17 лет. Мой IQ = 53.5. Я знаю, что ПИ=3.141592
print(name_text) # Я Вася. Мне 17 лет. Мой IQ = 53.5. Я знаю, что ПИ=3.141592

name = "Таня"
tanya_text = "Я {user_name}. Мне {user_age} лет. Мой IQ = {user_iq:.1f}. Я знаю, что ПИ={pi:.1f}" \
    .format(user_name=name, user_age=age, user_iq=iq, pi=pi)
print(tanya_text) # Я Таня. Мне 17 лет. Мой IQ = 53.5. Я знаю, что ПИ=3.1
