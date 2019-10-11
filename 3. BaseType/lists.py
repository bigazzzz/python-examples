man_user = ["Вася", 171, 100]
woman_user = ["Таня", 37, 33]
users = [man_user, woman_user]

print(man_user[0]) # Вася
print(man_user[0:1]) # ['Вася']
print(man_user[-1]) # 100
print(man_user[-1:]) # [100]
print(man_user[0:2]) # ['Вася', 17]
print(users[0][0]) # Вася
print(users[0]) # ['Вася', 17, 100]
print(users[1][1:3]) # [37,33]
print("-"*32)
man_user.reverse()
print(man_user)
#woman_user.sort() ERRRROR
woman_user.pop(0)
woman_user.insert(1,15)
woman_user.append(159)
woman_user.sort()
print(woman_user) # [15, 33, 37, 159]

