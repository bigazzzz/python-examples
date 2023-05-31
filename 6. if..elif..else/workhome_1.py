users = [ { "name": "Anton", "age": 20 },
          { "name": "Kirill", "age": 10 },
          { "name": "Michael", "age": 5 },
          { "name": "Alex", "age": 15 } ]


for user in users:
    if user['age']<3:
        status = 'младенец'
    elif user['age']<10:
        status = 'ребенок'
    elif user['age']<17:
        status = 'подросток'
    elif user['age']<25:
        status = 'молодой человек'
    elif user['age']<40:
        status = 'взрослый'
    else:
        status = 'старик'

    user['status'] = status
    print("Привет, меня зовут {user[name]}. мне {user[age]} лет и я {user[status]}".
                            format(user=user))

