user = {"name": "Вася", "age": 17, "organs": {"hands":2, "legs":2, "head":0}}
print(user)
print("Привет, меня зовут", user["name"])
print("Мне", user["age"])
print("У меня")
print("\tрук: ", user["organs"]["hands"])
print("\tног: ", user["organs"]["legs"])
print("\tголов: ", user["organs"]["head"])
print("ой "*10)
user["organs"]["head"] = 1
print("\tголов: ", user["organs"]["head"])
user["organs"]["body"]=1
print("\tи еще у меня есть " + str(user["organs"]["body"]) + " тело")
