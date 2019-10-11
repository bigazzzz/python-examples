name1 = "Вася"
age1 = 17
iq1 = 53.5
pi = 3.141592

text = "Я %(name)s. Мне %(age)d лет. Мой IQ = %(iq)d. Я знаю, что ПИ=%(pi)f" % {
    "name": name1,
    "age": age1,
    "iq": iq1,
    "pi": pi}

print(text)
# Я Вася. Мне 17 лет. Мой IQ = 53. Я знаю, что ПИ=3.141592

info = {
    "name": "Таня",
    "age": 30,
    "iq": 133.5,
    "pi": pi

}
text = "Я %(name)s. Мне %(age)d лет. Мой IQ = %(iq).2s. Я знаю, что ПИ=%(pi).1f" % info
print(text)
# Я Таня. Мне 30 лет. Мой IQ = 13. Я знаю, что ПИ=3.1
